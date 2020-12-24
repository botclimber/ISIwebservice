from flask import Flask, request, jsonify, render_template
import pymysql

from sec import Security
from auth import Auth
from recipes import Recipes

app = Flask(__name__)

db = pymysql.connect("localhost", "root", "", "quickrecipes")
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
@app.route('/api/v1/auth/name=<name>&email=<email>', methods=['GET'])
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


@app.route('/api/v1/recipe_details/', methods=['GET'])
def g_recipe_details():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Recipes(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gRecipeDetails()
	else:
		response = {'status': '400', 'message': 'invalid apiKey'}

	return jsonify(response)


if __name__ == "__main__":
	app.run(debug=True, port=5000)
