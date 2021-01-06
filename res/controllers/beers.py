import requests, json

class Beers:
	
	api_url = "https://api.punkapi.com/v2/beers"
	
	def gBeers(self, args = []):
		
		i = 0
		api_url = self.api_url	
	
		for x in args:
			if i == 1: api_url += "?{}={}".format(x, args.get(x))		
			elif i > 1: api_url += "&{}={}".format(x, args.get(x)) 
			i += 1
		
		return json.loads(requests.get(api_url).text)		

	

	def gBeerDetails(self, beer_id):
		
		api_url = "{}/{}".format(self.api_url, beer_id)
		return json.loads(requests.get(api_url).text)
	

	
	def gRandomBeer(self):
		
		api_url = "{}/random".format(self.api_url)
		return json.loads(requests.get(api_url).text)



	# recomend beer for recipe , it will search by recipe title/label/name so even if we dnt have the recipe id
	# wich means recipe doesnt exist in our database, we can still send our recomendation 
	def wBeersBetter(self, food_name):
		
		# recipe_name switch spaces by (_)
		food_name = food_name.replace(" ","_")
		
		api_url = "{}?food={}".format(self.api_url, food_name)
		r = json.loads(requests.get(api_url).text)		

		data = {'food': food_name, 'beers':{'results':len(r), 'beer_info':[] }}
		for x in r:
			data['beers']['beer_info'].append({'id': x['id'], 'name': x['name'], 'description': x['description'], 'abv': x['abv'], 'first_brewed': x['first_brewed'], 'fermentation': '{} {}'.format(x['method']['fermentation']['temp']['value'], x['method']['fermentation']['temp']['unit'])})
	
		return data


	

	def __del__(self):
		
		print("class Beers destroyed (BUMMMM!)")
