import dadesServer as d

class DAOUser:
    def __init__(self):
        self.users = d.users
    
    def getUserFromUsername(self, user):
        for u in self.users:
            if u.username == user :
                return u
        return None

class DAOChild:
    def __init__(self):
        self.children = d.children
        self.relations = d.relation_user_child
    
    def getChildIdFromUserId(self, id):
        for u in self.relations:
            if u.user_id == id :
                return u.child_id
        return None
    
    def getChildFromChildId(self, id):
        for c in self.children:
            if c.id == id:
                return c
        return None

    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email