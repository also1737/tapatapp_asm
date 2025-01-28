from flask import Flask, request, jsonify

# clase de usuari
class User:
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + " Username: " + self.username


# llista dels usuaris admesos
listUsers = [
    User(1, "pepe", "1234", "pepe@gmail.com"),
    User(2, "pepito", "2411", "pepito@gmail.com"),
    User(3, "pepazo", "54132", "pepazo@gmail.com"),
    User(4, "admin", "rootroot")
]

# clase que farem servir per accedir als usuaris
# DAO = Data Access Object
class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u.__dict__
        return None

daoUser = DAOUsers()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "hola hola"


@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n = str( request.args.get('name') )
    email = str( request.args.get('email') )
    return "hola hola nom: " + n + ", email: " + email



@app.route('/prototip/getuser/<string:user>', methods=['GET'])
def getUserPrototip(user):
    u = daoUser.getUserByUsername(user)
    if (u):
        return jsonify(u)
    else:
        return jsonify({"error":"usuari no trobat"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")