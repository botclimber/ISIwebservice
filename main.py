from flask import Flask, request, jsonify, render_template
import pymysql

from sec import Security
from auth import Auth
from recipes import Recipes

app = Flask(__name__)

db = pymysql.connect("localhost","root","","quickrecipes")
sec = Security(db)

# initial
@app.route('/', methods=['GET'])
def index():
	return render_template("api-doc.html")


@app.route('/api/v1/auth/name=<name>&email=<email>', methods=['GET'])
def auth(name, email):
	if sec.verify('email', email) == False:
		obj = Auth(name, email, db) # instance obj
		key = obj.cApiKey() # create ApiKey for this user
		obj.cUser(key) # create record in DB

	else:
		key = {'status': 500, 'message':'already exists an apiKey for this email'}

	return jsonify(key)

@app.route('/api/v1/recipes/', methods=['GET'])
def recipes():

	# call method to verify if apiKey exists
	if sec.verify('api_key', request.args.get('apiKey')):
		obj = Recipes(db, sec.gUserId(request.args.get('apiKey')), request.args)
		response = obj.gRecipes()
	else:
		response = {'status':'400','message':'invalid apiKey'}

	return jsonify(response)

if __name__ == "__main__":
	app.run(debug = True, port = 5000)
