import dadesServer as dades
import serverDAO as dao
from dadesServer import Error, User

class Registre:
    def __init__(self, user, passwd, email):
        self.user = user
        self.passwd = passwd
        self.email = email
    
    def validarUser(self):
        daoUsr = dao.DAOUser()
        result = daoUsr.getUserFromUsername(self.user)
        if isinstance(result, User): #usuario ya existe
            return Error("Usuari ya existeix")
        return None
    
    def crearUsuari(self):
        err = self.validarUser()
        if not err:
            u = User(self.user, self.passwd, self.email)
            dades.users.append(u)
        else:
            return err

print("==========[Registre de Usuari]==========")
user = input("introdueix nom de usuari: ")
email = input("introdueix correu electrònic: ")
paswd = str(input("introdueix contrasenya: "))

reg = Registre(user, paswd, email)

err = reg.crearUsuari()

if not err:
    for u in dades.users:
        print(u)
else:
    print(err)