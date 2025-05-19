from flask import Flask, request, jsonify
from serverDAO import DAOUser, DAOChild
from dadesServer import User, Error

app = Flask(__name__)
daoUser = DAOUser()
daoChild = DAOChild()

@app.route('/login', methods=['POST'])
def login():
    name = request.json['name']
    passwd = request.json['passwd']
    result = daoUser.login(name, passwd)
    if isinstance(result, User):
        return jsonify(result.__dict__), 200
    else:
        return jsonify({'error':result.getMessage()}), 400

@app.route('/childs', methods=['POST'])
def showChilds():
    name = request.json['name']
    auth_header = request.headers.get('Authorization')
    token_user = daoUser.tokens[name]

    if not auth_header or auth_header.split(" ")[1] != token_user:
        return jsonify({'Error': 'Accés no autoritzat'}), 401

    user = daoUser.getUserFromUsername(name)
    child_id = daoChild.getChildIdFromUserId(user.id)
    child = daoChild.getChildFromChildId(child_id)

    if isinstance(child, Error):
        return jsonify({'Error': child.getMessage()}), 200
    return (child.__dict__), 200

if __name__ == '__main__':
    app.run(debug=True, port="10101")