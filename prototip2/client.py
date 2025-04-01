import requests

url = "http://127.0.0.1:10101/login"

dades = {
    "name": "pare",
    "passwd": "123"
}

resposta = requests.post(url, json=dades)

if resposta.status_code == 200:
    print("Resposta: ", resposta.json())
else:
    print("Error", resposta.text)