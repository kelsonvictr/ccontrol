from datetime import datetime

from model.cartao import Cartao
from model.compra import Compra


def inicializar_ccs():
    cartoes = []
    cartoes.append(Cartao("nubank", 10, 12000))
    cartoes.append(Cartao("itau", 6, 20000))

    return cartoes


def cadastrar_compra():
    titulo = input("Digite o título da compra:")
    valor = input("Digite o valor da compra:")
    qtd_parcelas = input("Digite a qtd de parcelas:")
    data = input("Digite a data da compra:")

    compra = Compra(titulo, float(valor), int(qtd_parcelas), data)

    return compra


def visualizar_parcelas(compra):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]
    qtd_parcelas = compra.qtd_parcelas
    valor = compra.valor
    valor_parcela = valor / qtd_parcelas
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    parcelas = []
    mes_da_parcela = 0

    """
    Refatorar, depois, para atender parcelas que compreendam mais de 2 anos
    """
    for x in range(qtd_parcelas):
        if len(meses) - 1 < mes_atual + x:
            parcelas.append((ano_atual + 1, meses[mes_da_parcela], valor_parcela))
            mes_da_parcela = mes_da_parcela + 1
            continue

        parcelas.append((ano_atual, meses[mes_atual + x], valor_parcela))

    return parcelas


if __name__ == '__main__':
    cartoes = inicializar_ccs()
    compra = cadastrar_compra()
    print(visualizar_parcelas(compra))


