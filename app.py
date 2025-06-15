from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    return jsonify({'mensagem': f'Olá, {nome}!'})

@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    if not data or 'numero1' not in data or 'numero2' not in data:
        return jsonify({'erro': 'Por favor, forneça numero1 e numero2 no JSON'}), 400
    try:
        numero1 = float(data['numero1'])
        numero2 = float(data['numero2'])
        resultado = numero1 + numero2
        return jsonify({'soma': resultado})
    except (ValueError, TypeError):
        return jsonify({'erro': 'Os valores devem ser números válidos'}), 400

if __name__ == '__main__':
    app.run(debug=True)