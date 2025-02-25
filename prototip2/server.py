import dadesServer as dades
import serverDAO as dao
from dadesServer import User, Child, Tap, Status, Treatment

# Exemple d'ús de la llista d'usuaris
name = str(input())

daoUser = dao.DAOUser()

user = daoUser.getUserFromUsername(name)

print(user.__str__())

daoChild = dao.DAOChild()

id = daoChild.getChildIdFromUserId(user.id)

child = daoChild.getChildFromChildId(id)

print(child)
