from flask import Flask, request, jsonify

from services import create_user, list_users, create_event, list_event, delete_event, delete_user

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo'

@app.route('/login')
def login():
    pass # Fazer o login


@app.route('/usuarios', methods=["GET", "POST", "DELETE"])
def user():
    if request.method == "GET":
        users = list_users()
        return jsonify(users)
    if request.method == "POST":
        user = create_user(request.json)
        return jsonify(user)


@app.route('/deleta-usuario/<int:id>', methods=["DELETE"])
def deleteUser(id):
    if request.method == "DELETE":
        delete_user(id)
        return jsonify({"mensagem": "Usuário deletado com sucesso"})

@app.route('/eventos/<int:id>', methods=["GET", "POST", "DELETE"])
def event(id):
    if request.method == "GET":
        events = list_event(id)
        return jsonify(events)
    if request.method == "POST":
        event = request.json
        event["id_usuario"] = id
        result = create_event(event)
        return jsonify(result)
    if request.method == "DELETE":
        delete_event(id)
        return jsonify({"mensagem": "Evento deletado com sucesso"})


if __name__ == '__main__':
    app.run(port=3000)