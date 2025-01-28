import requests

user = input( "Introdueix nom d'usuari: " )

url = "http://192.168.144.171:10050/prototip/getuser/" + user

response = requests.get(url)

if response.status_code == 200:
    dadesUser = response.json()
    print(dadesUser)