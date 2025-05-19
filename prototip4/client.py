import requests


class Client:
    def __init__(self):
        self.url = "http://127.0.0.1:10101/"
        self.dades = {
            "name": "",
            "passwd": ""
        }
        self.hash = ""
        self.loggedIn = True

    def menu(self):
        option = -1
        while True:
            print("========[ TapatApp ]========")
            if self.loggedIn:
                print("1 - Veure Info infants a càrrec")
                print("0 - Tancar sessió")
            else:
                print("1 - Iniciar sessió")
                print("0 - Sortir")
                
            try:
                option = int(input("> "))
            except ValueError as v:
                option = -1

            match option:
                case 1:
                    if self.loggedIn:
                        self.consultarChilds()
                    else:
                        self.peticioLogin()
                    
                case 0:
                    if self.loggedIn:
                        self.loggedIn = False
                        self.esborrarDades()
                    else:
                        print("Sortint del programa...")
                        quit()
                    
                case _:
                    print("Opció incorrecta. Intenta de nou")


    def esborrarDades(self):
        self.dades["name"] = ""
        self.dades["passwd"] = ""
        self.hash = ""


    def dadesLogin(self):
        self.dades["name"] = input("Introdueix nom d'usuari o email: ")
        self.dades["passwd"] = input("Introdueix contrasenya: ")

    def peticioLogin(self):

        self.dadesLogin()
        try:
            resposta = requests.post(self.url + "login", json=self.dades)
            if resposta.status_code == 200:
                res = resposta.json()
                self.hash = res["hash"]
                self.loggedin = True
            else:
                return resposta.text
            
        except Exception as e:
            print(f"Error al connectar al servidor: {type(e).__name__}")

        

    def consultarChilds(self):

        dades = {
            "name": self.dades["name"]
        }
        headers = {
            "Authorization": "Bearer " + self.hash
        }

        try:
            resposta = requests.post(self.url + "childs", json=dades, headers=headers)

            if resposta.status_code == 200:
                print(resposta.text)
            else:
                print("Error: " , resposta.text)
        except Exception as e:
            print(f"Error al connectar al servidor: {type(e).__name__}")

if __name__ == '__main__':
    client = Client()
    client.menu()