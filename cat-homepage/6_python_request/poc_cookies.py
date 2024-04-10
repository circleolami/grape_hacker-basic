import requests


url = 'http://localhost:8000/page-babo.php'
data = {'username': 'babo', 'password': 'babo1234'}

cookies = {
    'user':'babo_bs'
}

response = requests.get(url, cookies=cookies,allow_redirects=False)

print(response.text)