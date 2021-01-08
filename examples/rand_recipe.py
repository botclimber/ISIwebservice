import requests

url = "http://127.0.0.1:5000/api/v1/rand_recipes/"

x = requests.get(url, headers={'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAxMTQ3MjZ9.2gx-CkIpjj08SMp46qMjAJ3WornzwvPYUVb1vZ2NhBA'})

print(x.text)
