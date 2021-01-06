import requests

url = "http://127.0.0.1:5000/api/v1/recipes/"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI5ZDFiNzgyMS02YzM5LTRiYzAtYWMxNC0xMzQ1Njg2YjVhNzEiLCJleHAiOjE2MDk5NTIyNTB9.WIKGbUK5kXVusOIpp0nsIlci75YRHvJvGGeqllgpr7w"})

print(x.text)
