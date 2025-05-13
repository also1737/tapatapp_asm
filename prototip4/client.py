import requests


class Client:
    def __init__(self):
        self.url = "http://127.0.0.1:10101/"
        self.dades = {
            "name": "",
            "passwd": ""
        }
        self.hash = ""
        self.loggedIn = False

    def menu(self):
        option = 0
        while True:
            print("========[ TapatApp ]========")
            if self.loggedIn:
                print("1 - Veure Info infants a càrrec")
                print("0 - Tancar sessió")
            else:
                print("1 - Login")
                print("0 - Sortir")

            match 

    def dadesLogin(self):
        self.dades["name"] = input("Introdueix nom d'usuari o email: ")
        self.dades["passwd"] = input("Introdueix contrasenya: ")

    def peticioLogin(self):

        self.dadesLogin()
        resposta = requests.post(self.url + "login", json=self.dades)

        if resposta.status_code == 200:
            res = resposta.json()
            self.hash = res["hash"]
        else:
            return resposta.text

    def consultarChilds(self):

        dades = {
            "name": self.dades["name"]
        }
        headers = {
            "Authorization": "Bearer " + self.hash
        }

        resposta = requests.post(self.url + "childs", json=dades, headers=headers)

        if resposta.status_code == 200:
            print(resposta.text)
        else:
            print("Error: " , resposta.text)

if __name__ == '__main__':
    client = Client()
    err = client.peticioLogin()
    print(err)
    print(client.hash)
    #client.consultarChilds()