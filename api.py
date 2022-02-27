import json

from flask import Flask, request

from control.ccontrol import cadastrar_cartao, cadastrar_compra, carregar_total_por_mes

app = Flask(__name__)


@app.route('/cartao', methods=['POST'])
def add_cartao():
    if request.method == 'POST':
        request_data = request.get_json()
        cadastrar_cartao(request_data['nome'], request_data['vencimento'], request_data['limite'])
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        return 405


@app.route('/compra', methods=['POST'])
def compra():
    if request.method == 'POST':
        request_data = request.get_json()
        cadastrar_compra(request_data['cartao_id'], request_data['titulo'], request_data['valor'],
                                  request_data['qtd_parcelas'])
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        return 405


@app.route('/compra/<cartao_id>/<mes>', methods=['GET'])
def add_compra(cartao_id, mes):
    if request.method == 'GET':
        return json.dumps(carregar_total_por_mes(int(cartao_id), int(mes))), 200, {'ContentType': 'application/json'}
    else:
        return 405


if __name__ == '__main__':
    app.run()
