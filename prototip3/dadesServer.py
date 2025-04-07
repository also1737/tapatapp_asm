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
    
users = [
    User("mare", "12345", "prova@gmail.com", ""),
    User("pare", "123", "prova2@gmail.com", "")
]
    
class Child:
    def __init__(self, id, name, sleepAverage, treatmentId, time):
        self.id = id
        self.name = name
        self.sleepAverage = sleepAverage
        self.treatmentId = treatmentId
        self.time = time

    def __str__(self):
        return self.name + ":" + str(self.sleepAverage) + ":" + str(self.time)
    

# Crear les classes Child, Tap, Role, Status i Treatment
children = [
    Child(1, "Carol Child", 8, 1, 6),
    Child(2, "Jaco Child", 10, 2, 6)
]

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

taps = [
    Tap(1, 1, 1, 1, "2024-12-18T19:42:43", "2024-12-18T20:42:43"),
    Tap(2, 2, 2, 2, "2024-12-18T21:42:43", "2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

class Role:
    def __init__(self, id, type):
        self.id = id
        self.type = type
    
    def __str__(self):
        return self.type

roles = [
    Role(1, 'Admin'),
    Role(2, 'Tutor Mare Pare'),
    Role(3, 'Cuidador'),
    Role(4, 'Seguiment')
]

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name

statuses = [
    Status(1, "sleep"),
    Status(2, "awake"),
    Status(3, "yes_eyepatch"),
    Status(4, "no_eyepatch")
]

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name

treatments = [
    Treatment(1, 'Hour'),
    Treatment(2, 'percentage')
]

user_token = {
}