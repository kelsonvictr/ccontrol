from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]
    qtd_parcelas = 18
    valor = 800.00
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
            parcelas.append((ano_atual+1, meses[mes_da_parcela], valor_parcela))
            mes_da_parcela = mes_da_parcela + 1
            continue

        parcelas.append((ano_atual, meses[mes_atual + x], valor_parcela))

    print(parcelas)
