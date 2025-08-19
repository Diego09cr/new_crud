from flask import Flask, request, jsonify
app = Flask(__name__)
usuarios = {}
id = 1

@app.route('/usuario', methods=['POST'])
def cria():
    global id
    dados = request.get_json()
    usuario = ({'id': id,
                'nome': dados.get('nome'),
               'idade': dados.get('idade'),
               'email': dados.get('email')})
    usuarios[id] = usuario
    id += 1
    return jsonify(usuario)

@app.route('/usuario/<int:id>', methods=['GET'])
def get_id(id):
    if id in usuarios:
        return jsonify(usuarios[id])
    else:
        return jsonify({'Usuário': 'Não existe'})
    
@app.route('/usuario/<int:id>', methods=['PUT'])
def att(id):
    if id in usuarios:
        dados = request.get_json()
        usuario = ({'id': id,
                'nome': dados.get('nome'),
               'idade': dados.get('idade'),
               'email': dados.get('email')})
        usuarios[id] = usuario
        return jsonify(usuario)
    else:
        return jsonify({'Usuário': 'Não existe'})

@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete(id):
    if id in usuarios:
        del(usuarios[id])
        return jsonify({"Usuário": "deleteado com sucesso"})
    else:
        return jsonify({'Usuário': 'Não encontrado'})


if __name__ == '__main__':
    app.run(debug=True)