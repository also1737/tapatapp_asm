from flask import Flask, request, jsonify
from serverDAO import DAOUser

app = Flask(__name__)
daoUser = DAOUser()


@app.route('/login', methods=['POST'])
def login():
    name = request.json['name']
    passwd = request.json['passwd']
    result = daoUser.login(name, passwd)
    if result:
        return jsonify(result.__dict__)
    else:
        return jsonify({'error':'usuari o contrasenya incorrectes'})

if __name__ == '__main__':
    app.run(debug=True, port="10101")