import mysql.connector
import hashlib
from dadesServer import Error, User

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tapatapp"
)

class DAOUser:

    def __init__(self):
        self.tokens = {

        }

    def getAllUsers(self):
        #return [user.__dict__ for user in self.users]
        cursor = connection.cursor()
        cursor.execute("select * from user")
        result = cursor.fetchall()
        res = []
        for row in result:
            res.append(row)
        cursor.close()
        return res

    def getUserFromUsername(self, user):
        cursor = connection.cursor(buffered=True)
        query = ("select username, passwd, email, hash from user where username = %s")
        data = (user, )
        cursor.execute(query, data)

        if cursor.rowcount == 0:
            return Error("Usuari no trobat")
        else:
            result = cursor.fetchone()
            user = User(
                result[0],
                result[1],
                result[2],
                result[3]
            )
            cursor.close()
            return user
    
    def getUserFromEmail(self, email):
        cursor = connection.cursor()
        query = ("select username, passwd, email, hash from user where email = %s")
        data = (email, )
        cursor.execute(query, email)
        if cursor.rowcount == 0:
            return Error("Usuari no trobat")
        else:
            user = User(
                cursor.fetchone()[0],
                cursor.fetchone()[1],
                cursor.fetchone()[2],
                cursor.fetchone()[3]
            )
            cursor.close()
            return user
    
    def login(self, name, passwd):
        user = self.getUserFromEmail(name) if name.find("@") != -1 else self.getUserFromUsername(name)
        if not isinstance(user, User) or user.password != passwd:
            return Error("Login incorrecte")
        else:
            token = hashlib.sha256()
            token.update(user.username.encode())
            token.update(user.email.encode())
            self.tokens.update( {user.username: token.hexdigest()} )
            print(self.tokens)
            user.hash = token.hexdigest()
            return user
        
    def validarUser(self, user):
        result = self.getUserFromUsername(user)
        if isinstance(result, User): #usuario ya existe
            return Error("Usuari ya existeix")
        return None
    
    def crearUser(self, user, passwd, email):
        err = self.validarUser()
        if not err:
            u = User(user, passwd, email)
            d.users.append(u)
        else:
            return err

class DAOChild:

    def getAllChildren(self):
        return [child.__dict__ for child in self.children]
    
    def getChildIdFromUserId(self, id):
        for r in self.relations:
            if r['user_id'] == id :
                return r['child_id']
        return Error("Child no trobat")
    
    def getChildFromChildId(self, id):
        for c in self.children:
            if c.id == id:
                return c
        return Error("Child no trobat")

    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email