import requests


class Client:
    def __init__(self):
        self.url = "http://127.0.0.1:10101/"
        self.dades = {
            "username": "",
            "passwd": ""
        }
        self.hash = ""
        self.loggedIn = False

    def menu(self):
        option = -1
        while True:
            print("\n\n========[ TapatApp ]========")
            if self.loggedIn:
                print(f"Sessió iniciada com a {self.dades['username']}")
                print("1 - Veure Info infants a càrrec")
                print("2 - Veure tractament infant")
                print("0 - Tancar sessió")
            else:
                print("1 - Iniciar sessió")
                print("0 - Sortir")
                
            try:
                option = int(input("> "))
                print()
            except ValueError:
                option = -1

            match option:
                case 1:
                    if self.loggedIn:
                        self.consultarChilds()
                    else:
                        self.peticioLogin()

                case 2:
                    if self.loggedIn:
                        self.veureTractament()
                    
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
        self.dades["username"] = ""
        self.dades["passwd"] = ""
        self.hash = ""

    def dadesLogin(self):
        self.dades["username"] = input("Introdueix nom d'usuari o email: ")
        self.dades["passwd"] = input("Introdueix contrasenya: ")

    def peticioLogin(self):

        self.dadesLogin()
        try:
            resposta = requests.post(self.url + "login", json=self.dades)


            res = resposta.json()

            if resposta.status_code == 200:
                self.hash = res["hash"]
                self.loggedIn = True

                print(f"Sessió iniciada. Benvolgut/da, {res['username']}")

            else:
                
                print(res["error"])
        except (ConnectionError, ConnectionRefusedError) as e:
            print(f"Error al connectar al servidor: {type(e).__name__}")

    def consultarChilds(self):

        dades = {"username": self.dades["username"]}
        headers = {"Authorization": "Bearer " + self.hash}

        try:
            resposta = requests.post(self.url + "childs", json=dades, headers=headers)

            if resposta.status_code == 200:

                resultat = resposta.json()
                
                print("Id\t|Name\t\t|Sleep\t|Treatment\t|Time")
                print("------------------------------------------------------")

                for row in resultat:
                    print(f"{row[0]}\t|{row[1]}\t|{row[2]}\t|{row[3]}\t\t|{row[4]}")

            else:

                print("Error: " , resposta.text)

        except Exception as e:
            print(f"Error al connectar al servidor: {type(e).__name__}")

    def veureTractament(self):

        self.consultarChilds()
        child_id = int(input("Introdueix ID de l'infant: "))

        



if __name__ == '__main__':
    client = Client()
    client.menu()