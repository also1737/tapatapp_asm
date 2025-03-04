import serverDAO as dao
from dadesServer import Error, User

class Login: #classe que controla el login
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def validar(self):
        daoUser = dao.DAOUser()
        user = daoUser.getUserFromUsername(self.name)
        if not user or user.password != self.passwd:
            return Error("Usuari o contrasenya incorrecta")
        else:
            print(f"Login correcte, benvingut {self.name}")
            return user