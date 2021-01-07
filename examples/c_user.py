import requests

url = 'http://127.0.0.1:5000/api/v1/auth/'
obj = {'name':'Duarte Silva', 'password': '246810', 'email':'duarte@admin.pt', 'user_type':'colab'}

x = requests.post(url, json = obj)

print(x.text)
