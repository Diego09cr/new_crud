from flask import Flask, request, jsonify
app = Flask(__name__)
users = {}
id = 1

@app.route('/User', methods=['POST'])
def cria():
    global id
    dados = request.get_json()
    User = ({
        'id': id,
        'name': dados.get('name'),
        'age': dados.get('age'),
        'email': dados.get('email')
        })
    users[id] = User
    id += 1
    return jsonify(User)

@app.route('/User/<int:id>', methods=['GET'])
def get_id(id):
    if id in users:
        return jsonify(users[id])
    else:
        return jsonify({'User': 'Not found'})
    
@app.route('/User/<int:id>', methods=['PUT'])
def att(id):
    if id in users:
        dados = request.get_json()
        User = ({
            'id': id,
            'name': dados.get('name'),
            'age': dados.get('age'),
            'email': dados.get('email')
            })
        users[id] = User
        return jsonify(User)
    else:
        return jsonify({'User': 'Not found'})

@app.route('/User/<int:id>', methods=['DELETE'])
def delete(id):
    if id in users:
        del(users[id])
        return jsonify({"User": "Deleted successfully"})
    else:
        return jsonify({'User': 'Not found'})


if __name__ == '__main__':
    app.run(debug=True)