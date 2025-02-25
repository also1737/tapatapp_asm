import dadesServer as d

class DAOUser:
    def __init__(self):
        self.users = d.users
    
    def getAllUsers(self):
        return [user.__dict__ for user in self.users]

    def getUserFromUsername(self, user):
        print(user)
        for u in self.users:
            if u.username == user :
                return u
        return None

class DAOChild:
    def __init__(self):
        self.children = d.children
        self.relations = d.relation_user_child

    def getAllChildren(self):
        return [child.__dict__ for child in self.children]
    
    def getChildIdFromUserId(self, id):
        for r in self.relations:
            print(r)
            if r['user_id'] == id :
                return r['child_id']
        return None
    
    def getChildFromChildId(self, id):
        for c in self.children:
            if c.id == id:
                return c
        return None

    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email