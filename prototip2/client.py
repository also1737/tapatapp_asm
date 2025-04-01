import requests


class Client:
    def __init__(self):
        self.url = "http://127.0.0.1:10101/login"
        self.dades = {
            "name": "",
            "passwd": ""
        }
        self.hash = ""

    def dadesLogin(self):
        self.dades["name"] = input("Introdueix nom d'usuari o email: ")
        self.dades["passwd"] = input("Introdueix contrasenya: ")

    def peticioLogin(self):

        self.dadesLogin()
        resposta = requests.post(self.url, json=self.dades)

        if resposta.status_code == 200:
            res = resposta.json()
            self.hash = res["hash"]
        else:
            return resposta.text

if __name__ == '__main__':
    client = Client()
    res = client.peticioLogin()
    print(res)
    print(client.hash)