import requests


# url = "http://127.0.0.1:5000/api/v1/create_recipe/"

# obj = {'apiKey': 'Nr4SRPJg0mZnhw','title':'tonescos', 'instructions': '- cozinhar 300 graus e durante 30min', 'description':' sadasdasd dasd ', 'fat': 283, 'id': [1,2], 'amount': [1, 6] }

# x = requests.post(url, json = obj)



# url = "http://127.0.0.1:5000/api/v1/update_recipe/19"
# obj = {'apiKey': 'Nr4SRPJg0mZnhw','title':'Ramen', 'instructions': 'caldo de carne, molho de soja, peço desculpa ', 'description':'muito bom, 99.9% saudavel','calories': 19, 'fat':25, 'id_ingredients':[2], 'amount':[4] }

# x = requests.put(url, json = obj)


url = "http://127.0.0.1:5000/api/v1/delete_recipe/20"
obj = {'apiKey': 'Nr4SRPJg0mZnhw'}

x = requests.delete(url, json = obj)

print(x.text)
