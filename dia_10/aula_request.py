import requests
resposta = requests.get('https://jw.org')
print(resposta.status_code)