from flask import Flask, request, jsonify, render_template, make_response
import mysql.connector
from mysql.connector import errorcode
import jwt
import datetime

from functools import wraps
from res.sec import Security
from res.auth import Auth
from res.controllers.recipes import Recipes
from res.controllers.ingredients import Ingredients
from res.controllers.beers import Beers

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = '21savageinjapan'

#config = {
#'host':'qkrecipes.mysql.database.azure.com',
#'user':'sorte@qkrecipes',
#'password':'wegotFlow21',
#'database':'quickrecipes',
#}

config = {
'host':'localhost',
'user':'root',
'password':'',
'database':'quickrecipes',
}

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





# ****************************
# *          AUTH            *
# ****************************
"""
	With this app.route we check and create a new user if doesn't exist
"""

# CREATE USER
@app.route('/api/v1/auth/', methods=['POST'])
def auth():
	"""

	:param name: user name
	:param email: user email

	:return: a key
	"""
	data = request.get_json()
	obj = Auth(db, data['email'], data['password'], data['name']) if 'user_type' not in data else Auth(db, data['email'], data['password'], data['name'], data['user_type'])  # instance obj
	response = obj.cUser()  # create record in DB

	return jsonify(response)


# LOGIN 
@app.route('/api/v1/login/')
def login():
	
	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})

	user_obj = Auth(db, auth.username, auth.password)
	user = user_obj.get_user()	
	
	if not user:		
		return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})
	
	if user_obj.check_password(user['password']):
		token = jwt.encode({'public_id': user['public_id'], 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'], algorithm="HS256")
		return jsonify({'token': token})
	
	return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})


# SESSION VERIFICATION
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message': 'Token is missing!'}), 401
				
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
			current_user = Auth(db).get_by_pi(data['public_id'])
		except:
			return jsonify({'message': 'Token is invalid'}), 401

		return f(current_user, *args, **kwargs)
	
	return decorated





# ****************
# * GET REQUESTS *
# ****************

"""
	With this app.route we can get all recipes with or without filters
"""
@app.route('/api/v1/recipes/', methods=['GET'])
@token_required
def recipes(current_user):

	obj = Recipes(db, current_user['user_id'], request.args)
	response = obj.gRecipes()

	return jsonify(response)




@app.route('/api/v1/rand_recipes/', methods=['GET'])
@token_required
def g_random_recipe(current_user):

	obj = Recipes(db, current_user['user_id'], request.args)
	recipes = obj.gRecipes() # get all recipes
	response = obj.gRandomRecipes(recipes) # send all recipes to the method gRandomRecipe and then it choses one randomly
	return jsonify(response)



@app.route('/api/v1/recipe_details/<int:recipe_id>', methods=['GET'])
@token_required
def g_recipe_details(current_user, recipe_id):

	obj = Recipes(db, current_user['user_id'], request.args)
	response = obj.gRecipeDetails(recipe_id)
	
	return jsonify(response)




# INGREDIENTS
@app.route('/api/v1/ingredients/', methods=['GET'])
@token_required
def ingredients(current_user):

	obj = Ingredients(db, current_user['user_id'], request.args)
	response = obj.gIngredients()

	return jsonify(response)



@app.route('/api/v1/ingredient_details/<ing_id>', methods=['GET'])
@token_required
def g_ingredients_details(current_user, ing_id):

	obj = Ingredients(db, current_user['user_id'], request.args)
	response = obj.gIngredientDetails(ing_id)

	return jsonify(response)




# BEERS
@app.route('/api/v1/beers/', methods=['GET'])
@token_required
def beers(current_user):

	obj = Beers()
	response = obj.gBeers(request.args)

	return jsonify(response)



@app.route('/api/v1/beers/<int:beer_id>', methods=['GET'])
@token_required
def g_beer_details(current_user, beer_id):

	obj = Beers()
	response = obj.gBeerDetails(beer_id)

	return jsonify(response)



@app.route('/api/v1/beers/random', methods=['GET'])
@token_required
def random_beer(current_user):

	obj = Beers()
	response = obj.gRandomBeer()

	return jsonify(response)



@app.route('/api/v1/beers/<food_name>', methods=['GET'])
@token_required
def w_beers_better(current_user, food_name):

	obj = Beers()
	response = obj.wBeersBetter(food_name)

	return jsonify(response)


# *****************
# * POST REQUESTS *
# *****************

@app.route('/api/v1/create_recipe/', methods=['POST'])
@token_required
def create_recipe(current_user):
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Recipes(db, current_user['user_id'], data)
	response = obj.cRecipe()	
	
	return jsonify(response)



@app.route('/api/v1/create_ingredient/', methods=['POST'])
@token_required
def create_ingredient(current_user):
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Ingredients(db, current_user['user_id'], data)
	response = obj.cIngredient()	
	
	return jsonify(response)



# ****************
# * PUT REQUESTS *
# ****************

@app.route('/api/v1/update_recipe/<int:recipe_id>', methods=['PUT'])
@token_required
def update_recipe(current_user, recipe_id):
	
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Recipes(db, current_user['user_id'], data)
	response = obj.uRecipe(recipe_id)	
	
	return jsonify(response)




@app.route('/api/v1/update_ingredient/<int:ing_id>', methods=['PUT'])
@token_required
def update_ingredient(current_user, ing_id):
	
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Ingredients(db, current_user['user_id'], data)
	response = obj.uIngredient(ing_id)	
	
	return jsonify(response)



# *******************
# * DELETE REQUESTS *
# *******************

@app.route('/api/v1/delete_recipe/<int:recipe_id>', methods=['DELETE'])
@token_required
def delete_recipe(current_user, recipe_id):
	
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Recipes(db, current_user['user_id'])
	response = obj.dRecipe(recipe_id)
	
	return jsonify(response)




@app.route('/api/v1/delete_ingredient/<int:ing_id>', methods=['DELETE'])
@token_required
def delete_ingredient(current_user, ing_id):
	
	if current_user['user_type'] != 'colab':
		return jsonify({'message': 'cannot perform that function'})
	
	data = request.get_json()
	
	obj = Ingredients(db, current_user['user_id'])
	response = obj.dIngredient(ing_id)
	
	return jsonify(response)




if __name__ == "__main__":
	app.run(debug=True, port=5000)
