import requests
  
url = "http://127.0.0.1:5000/api/v1/beers/"

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyMzM0MDJ9.eJeM9Q3va5WpxfpWENxG4kHwirdGCWpKgB4apuXvJEQ"})

print(x.text)
