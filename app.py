from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import errorcode

from res.sec import Security
from res.auth import Auth
from res.controllers.recipes import Recipes
from res.controllers.ingredients import Ingredients
from res.controllers.beers import Beers

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

config = {
'host':'qkrecipes.mysql.database.azure.com',
'user':'sorte@qkrecipes',
'password':'wegotFlow21',
'database':'quickrecipes',
}

#config = {
#'host':'localhost',
#'user':'root',
#'password':'',
#'database':'quickrecipes',
#}

# Construct connection string
try:
   db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

sec = Security(db)


"""
	With this app.route we go to the Home page
"""
@app.route('/', methods=['GET'])
def index():
	return render_template("api-doc.html")


"""
	With this app.route we check and create a new user if doesn't exist
"""
@app.route('/api/v1/auth/<name>&<email>', methods=['GET'])
def auth(name, email):
	"""

	:param name: user name
	:param email: user email

	:return: a key
	"""
	if not sec.verify('email', email):
		obj = Auth(name, email, db)  # instance obj
		key = obj.cApiKey()  # create ApiKey for this user
		obj.cUser(key)  # create record in DB

	else:
		key = {'status': 500, 'message':'already exists an apiKey for this email'}

	return jsonify(key)



# ****************
# * GET REQUESTS *
# ****************

"""
	With this app.route we can get all recipes with or without filters
"""
@app.route('/api/v1/recipes/', methods=['GET'])
def recipes():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Recipes(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gRecipes()
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)




@app.route('/api/v1/rand_recipes/', methods=['GET'])
def g_random_recipe():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Recipes(db, sec.gUserId(request.args.get('apiKey')), request.args)
		recipes = obj.gRecipes() # get all recipes
		response = obj.gRandomRecipes(recipes) # send all recipes to the method gRandomRecipe and then it choses one randomly
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/recipe_details/<int:recipe_id>', methods=['GET'])
def g_recipe_details(recipe_id):

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Recipes(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gRecipeDetails(recipe_id)
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)





# INGREDIENTS
@app.route('/api/v1/ingredients/', methods=['GET'])
def ingredients():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Ingredients(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gIngredients()
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/ingredient_details/<ing_id>', methods=['GET'])
def g_ingredients_details(ing_id):

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Ingredients(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gIngredientDetails(ing_id)
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)




# BEERS
@app.route('/api/v1/beers/', methods=['GET'])
def beers():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Beers()
		response = obj.gBeers(request.args)
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/beers/<int:beer_id>', methods=['GET'])
def g_beer_details(beer_id):

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Beers()
		response = obj.gBeerDetails(beer_id)
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/beers/random', methods=['GET'])
def random_beer():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Beers()
		response = obj.gRandomBeer()
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/beers/<food_name>', methods=['GET'])
def w_beers_better(food_name):

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Beers()
		response = obj.wBeersBetter(food_name)
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)


# *****************
# * POST REQUESTS *
# *****************

@app.route('/api/v1/create_recipe/', methods=['POST'])
def create_recipe():
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Recipes(db, sec.gUserId(data['apiKey']), data)
		response = obj.cRecipe()	
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



@app.route('/api/v1/create_ingredient/', methods=['POST'])
def create_ingredient():
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Ingredients(db, sec.gUserId(data['apiKey']), data)
		response = obj.cIngredient()	
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



# ****************
# * PUT REQUESTS *
# ****************

@app.route('/api/v1/update_recipe/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Recipes(db, sec.gUserId(data['apiKey']), data)
		response = obj.uRecipe(recipe_id)	
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)




@app.route('/api/v1/update_ingredient/<int:ing_id>', methods=['PUT'])
def update_ingredient(ing_id):
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Ingredients(db, sec.gUserId(data['apiKey']), data)
		response = obj.uIngredient(ing_id)	
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)



# *******************
# * DELETE REQUESTS *
# *******************

@app.route('/api/v1/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Recipes(db, sec.gUserId(data['apiKey']))
		response = obj.dRecipe(recipe_id)
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)




@app.route('/api/v1/delete_ingredient/<int:ing_id>', methods=['DELETE'])
def delete_ingredient(ing_id):
	
	data = request.get_json()
	
	# call method to verify if apiKey exists
	if sec.verify('api_key', data['apiKey']): 
		obj = Ingredients(db, sec.gUserId(data['apiKey']))
		response = obj.dIngredient(ing_id)
	
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)




if __name__ == "__main__":
	app.run(debug=True, port=5000)
