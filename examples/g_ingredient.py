import requests
  
url = "http://127.0.0.1:5000/api/v1/ingredient_details/2"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAxMjMyMTJ9.faptW9Fn163bRrTUcTCRSxnRLJWbiVqy2DNODF8aBnc"})

print(x.text)
