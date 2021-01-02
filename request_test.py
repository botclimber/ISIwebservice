import requests

# url = "http://127.0.0.1:5000/api/v1/create_ingredient/"

# obj = {'apiKey': 'Nr4SRPJg0mZnhw','name':'canela', 'type': 'pó mágico' }
# x = requests.post(url, json = obj)



url = "http://127.0.0.1:5000/api/v1/update_ingredient/5"
obj = {'apiKey': 'Nr4SRPJg0mZnhw','name_ds':'123123', 'calories': 12, 'type':'fruit' }

x = requests.put(url, json = obj)


# url = "http://127.0.0.1:5000/api/v1/delete_recipe/20"
# obj = {'apiKey': 'Nr4SRPJg0mZnhw'}

# x = requests.delete(url, json = obj)

print(x.text)
