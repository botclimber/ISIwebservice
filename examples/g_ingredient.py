import requests
  
url = "http://127.0.0.1:5000/api/v1/ingredient_details/3"
# obj = {'lite': 1}

x = requests.get(url, headers={"Content-Type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAyMjM3NDV9.rkIEDiVBQ4IOpQ5P8MmfE6bz7E8Fc6uiz5hFf4dyzJw"})

print(x.text)
