import requests

respostas=requests.get('https://api.github.com')
print(f"{respostas.status_code}")