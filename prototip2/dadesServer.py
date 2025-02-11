# Dades d'exemple amb List
# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email
    
users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]
    
class Child:
    def __init__(self, id, name, sleepAverage, treatmentId, time):
        self.id = id
        self.name = name
        self.sleepAverage = sleepAverage
        self.treatmentId = treatmentId
        self.time = time

# Crear les classes Child, Tap, Role, Status i Treatment
children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

class Tap:
    def __init__(self, id, childId, statusId, userId, init, end):
        self.id = id
        self.childId = childId
        self.statusId = statusId
        self.userId = userId
        self.init = init
        self.end = end

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
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

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]
