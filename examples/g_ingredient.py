import requests
  
url = "http://quickrecipe.azurewebsites.net/api/v1/ingredient_details/3"
# obj = {'lite': 1}

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyMjQ3MDh9.4cse23HSuh3EnK6D2G0BscnP7OsOqoU55kDP5yBXAz8"})

print(x.text)
