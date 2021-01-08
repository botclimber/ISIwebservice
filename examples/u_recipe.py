import requests
  
url = "http://127.0.0.1:5000/api/v1/update_recipe/25"
obj = {'title': 'teset de asdasd'}

r = requests.put(url, json = obj, headers = {'x-access-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI3YWNjOGRiMy1hOWViLTQxNGQtYjQ5Yi05M2NmNGY4MGVkZDEiLCJleHAiOjE2MTAxMjU4NDF9.cYAFVWLccMjpSrMJd69V-ie4UC-EfMcmIfmnDo4JsXk'})

print(r.text)
