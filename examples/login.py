import requests

url = "http://127.0.0.1:5000/api/v1/login/"

r = requests.get(url, auth=('carlos@admin.pt','greedisgood'))

print(r.text)