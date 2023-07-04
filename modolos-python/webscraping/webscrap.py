# requests pra requisições HTTP
import requests

# http:// -> 8080
# https:// -> 443
url = 'http://localhost:7777/'
response = requests.get(url)


print(response.text)
