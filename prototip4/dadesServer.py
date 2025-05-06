# Dades d'exemple amb List

class Error:
    def __init__(self, errorMsg):
        self.errorMsg = errorMsg
    
    def message(self):
        return "Error: " + self.errorMsg

# Clase User
class User:

    user_id = 0

    def __init__(self, username, password, email, hash):
        self.id = User.user_id
        User.user_id += 1
        self.username = username
        self.password = password
        self.email = email
        self.hash = hash
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email  + ":" + str(self.id)
    
class Child:
    def __init__(self, id, name, sleepAverage, treatmentId, time):
        self.id = id
        self.name = name
        self.sleepAverage = sleepAverage
        self.treatmentId = treatmentId
        self.time = time

    def __str__(self):
        return self.name + ":" + str(self.sleepAverage) + ":" + str(self.time)

class Tap:
    def __init__(self, id, childId, statusId, userId, init, end):
        self.id = id
        self.childId = childId
        self.statusId = statusId
        self.userId = userId
        self.init = init
        self.end = end

    def __str__(self):
        return self.init + ":" + self.end
    
class Role:
    def __init__(self, id, type):
        self.id = id
        self.type = type
    
    def __str__(self):
        return self.type

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name
