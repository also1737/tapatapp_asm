import requests

#classe d'usuari
class User:
    def __init__(self, id, username, password, email=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def mostrar(self):
        return "Id: " + str(self.id) + "\nUsername: " + self.username + "\nEmail: " + self.email

#classe d'error
class Error:
    def __init__(self, errorMsg):
        self.errorMsg = errorMsg
    
    def mostrar(self):
        return "Error: " + self.errorMsg

#classe que realitza les petitcions al servidor
class DAOUser:
    def __init__(self, user):
        self.username = user

    def getUsuariServer(self):

        url = "http://192.168.144.171:10050/prototip/getuser/" + self.username

        #fem la connexió al servidor, si falla retornem un error
        try:
            response = requests.get(url)
        except Exception:
            err = Error("no s'ha pogut connectar al servidor")
            return err

        #si ens hem pogut connectar, processem la petició
        if response.status_code == 200:
            dades = response.json()

            #si hi ha un camp "id" en dades, hem trobat l'usuari
            if "id" in dades :
                u = User(dades["id"], dades["username"], dades["password"], dades["email"])
                return u
            #si no, no hem trobat l'usuari i retornem error
            else:
                e = Error(dades["error"])
                return e
        
        else:
            err = Error(response.status_code)
            return err
            
#classe que mostrará la informació a l'usuari
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
    
#funció principal
if __name__ == '__main__':

    v = View()

    v.getUsuariInput()

    daoUser = DAOUser(v.username)

    u = daoUser.getUsuariServer()

    if isinstance(u, User):
        v.mostrarUsuari(u)
    else:
        v.mostrarError(u)

