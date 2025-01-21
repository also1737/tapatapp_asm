from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + " Username: " + self.username

listUsers = [
    User(1, "pepe", "1234", "pepe@gmail.com"),
    User(2, "pepito", "2411", "pepito@gmail.com"),
    User(3, "pepazo", "54132", "pepazo@gmail.com"),
    User(4, "admin", "rootroot")
]

class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self, username):
        for u in self.users:
            if u.username == username:
                return u
        return None

daoUser = DAOUsers()

app = Flask(__name__)

@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n = str( request.args.get('name') )
    email = str( request.args.get('email') )
    return "hola hola nom: " + n + ", email: " + email

@app.route('/prototip/getuser/<string:user>', methods=['GET'])
def provaGetUser(user):
    return "usuari: " + user

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")