import json
from datetime import datetime

from sqlalchemy import and_

from model.cartao import Cartao
from model.compra import Compra
from model.sqlalchemy_start import sqlalchemy_starter

Session, Base, engine = sqlalchemy_starter()

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]


def cadastrar_cartao(nome, vencimento, limite):
    cartao = Cartao(nome, int(vencimento), float(limite))
    Base.metadata.create_all(engine)
    session = Session()
    session.add(cartao)
    session.commit()
    session.close()


def cadastrar_compra(cartao_id, titulo, valor, qtd_parcelas):
    item = Compra(int(cartao_id), titulo, float(valor), int(qtd_parcelas), datetime.today())
    Base.metadata.create_all(engine)
    session = Session()
    session.add(item)
    session.commit()
    session.close()


def visualizar_parcelas(compra):
    titulo = compra.titulo
    qtd_parcelas = compra.qtd_parcelas
    valor = compra.valor
    valor_parcela = valor / qtd_parcelas
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    data = compra.data
    parcelas = []
    mes_da_parcela = 0

    """
    Refatorar, depois, para atender parcelas que compreendam mais de 2 anos
    """
    for x in range(qtd_parcelas):
        if len(meses) - 1 < mes_atual + x:
            parcelas.append((ano_atual + 1, titulo, meses[mes_da_parcela], valor_parcela, data))
            mes_da_parcela = mes_da_parcela + 1
            continue

        parcelas.append((ano_atual, titulo, meses[mes_atual + x], valor_parcela, data))

    return parcelas


def carregar_total_por_mes(cartao_id, mes):
    mes = meses[mes - 1]
    session = Session()
    dados = session.query(Compra).filter(Compra.cartao_id == cartao_id)
    parcelas_do_mes = []
    for compra in dados:
        for parcela in visualizar_parcelas(compra):
            if parcela[2] == mes:
                print(parcela)
                parcelas_do_mes.append(
                    {
                        "titulo": parcela[1],
                        "mes": parcela[2],
                        "valor": parcela[3],
                        "data": str(parcela[4])
                    }
                )
    #total_do_mes = sum(item['valor'] for item in parcelas_do_mes)
    #print(f'Compras do mês de {mes}: {parcelas_do_mes} \nTotal: {total_do_mes}')

    return parcelas_do_mes

