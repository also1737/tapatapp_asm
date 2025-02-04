import requests

class User:
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def mostrar(self):
        return "Id: " + str(self.id) + "\nUsername: " + self.username + "\nEmail: " + self.email

class Error:
    def __init__(self, errorMsg):
        self.errorMsg = errorMsg
    
    def mostrar(self):
        return "Error: " + self.errorMsg

class DAOUser:
    def __init__(self, user):
        self.username = user

    def getUsuariServer(self):

        url = "http://192.168.144.171:10050/prototip/getuser/" + self.username

        try:
            response = requests.get(url)
        except Exception:
            err = Error("no s'ha pogut connectar al servidor")
            return err

        if response.status_code == 200:
            dades = response.json()
            if "id" in dades :
                u = User(dades["id"], dades["username"], dades["password"], dades["email"])
                return u
            else:
                e = Error(dades["error"])
                return e
        else:
            err = Error(response.status_code)
            return err
            

class View:
    def __init__(self):
        self.username = ""

    def getUsuariInput(self):
        user = input( "Introdueix nom d'usuari: " )
        self.username = user

    def mostrarUsuari(self, user):
        print( user.mostrar() )

    def mostrarError(self, error):
        print( error.mostrar() )
    

if __name__ == '__main__':

    v = View()

    v.getUsuariInput()

    daoUser = DAOUser(v.username)

    u = daoUser.getUsuariServer()

    if isinstance(u, User):
        v.mostrarUsuari(u)
    else:
        v.mostrarError(u)

