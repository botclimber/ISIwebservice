import requests

url = "http://127.0.0.1:5000/api/v1/recipes/"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAxNDY4NDl9.wSRbQPDCd7C2Z72xVdkujP5pRh80Un3guwqeIN95PSk"})

print(x.text)
