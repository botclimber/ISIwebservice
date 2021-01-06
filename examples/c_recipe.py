import requests

url = "http://127.0.0.1:5000/api/v1/create_recipe/"
obj = {'title': 'teset de teste', 'instructions': '21 smiles', 'id':[2,3], 'amount':[12,28]}

r = requests.post(url, json = obj, headers = {'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3M2ZmNWFhMy0yMTI4LTQxOTctOTliYS04MjJkNWRiNWQ4OWYiLCJleHAiOjE2MDk5NTIyOTh9.cRwW4tEBQHAW1-l7Qv7CYYlo9Hv8m0U70nyW-NvtiBo'})

print(r.text)
