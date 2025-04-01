import dadesServer as d
import hashlib
from dadesServer import Error, User

class DAOUser:
    def __init__(self):
        self.users = d.users
        self.tokens = d.user_token
    
    def getAllUsers(self):
        return [user.__dict__ for user in self.users]

    def getUserFromUsername(self, user):
        for u in self.users:
            if u.username == user :
                return u
        return None
    
    def getUserFromEmail(self, user):
        for u in self.users:
            if u.email == user :
                return u
        return None
    
    def login(self, name, passwd):
        user = self.getUserFromEmail(name) if name.find("@") != -1 else self.getUserFromUsername(name)
        if not user or user.password != passwd:
            return None
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
    def __init__(self):
        self.children = d.children
        self.relations = d.relation_user_child

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