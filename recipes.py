# waiting signature
from api_standard_service import Api_standard_service

import datetime
import numpy
import random

class Recipes(Api_standard_service):

	
	def gRecipes(self):
		"""
		Method that search for recipes
		:param self: object with all information for the search
		:type param: object
		:return: return a array of recipe

		"""
		sql = "SELECT Recipe.title, Recipe.id_recipe, Recipe.image_link, Nutrition.calories, Nutrition.carbs, Nutrition.fat, Nutrition.protein, Nutrition.fiber FROM Recipe, Nutrition WHERE Recipe.id_nutrition = Nutrition.id_nutrition and (visible = 1 or (visible = 0 and id_user = {})) ".format(self.user_id)

		sql += " and fiber > {}".format(self.args.get('minFiber')) if self.args.get('minFiber') != None else ""
		sql += " and fiber < {}".format(self.args.get('maxFiber')) if self.args.get('maxFiber') != None else ""

		sql += " and calories > {}".format(self.args.get('minCals')) if self.args.get('minCals') != None else ""
		sql += " and calories < {}".format(self.args.get('maxCals')) if self.args.get('maxCals') != None else ""

		sql += " and protein > {}".format(self.args.get('minProtein')) if self.args.get('minProtein') != None else ""
		sql += " and protein < {}".format(self.args.get('maxProtein')) if self.args.get('maxProtein') != None else ""

		sql += " and carbs > {}".format(self.args.get('minCarbs')) if self.args.get('minCarbs') != None else ""
		sql += " and carbs < {}".format(self.args.get('maxCarbs')) if self.args.get('maxCarbs') != None else ""

		sql += " and fat > {}".format(self.args.get('minFat')) if self.args.get('minFat') != None else ""
		sql += " and fat < {}".format(self.args.get('maxFat')) if self.args.get('maxFat') != None else ""

		sql += " ORDER BY {} {}".format(self.args.get('sort'), self.args.get('sortDirection').upper()) if self.args.get('sort') != None else ""

		sql += " LIMIT {}".format(self.args.get('results')) if self.args.get('results') != None else ""

		# run sql var
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()

			data = {'results': [], 'nr_results': len(results)}
			for x in results:
				data['results'].append({'id': x[1],'calories': x[3], 'carbs': x[4], 'fat': x[5], 'protein': x[6], 'fiber': x[7], 'image': x[2], 'imageType': 'jpg,jpeg', 'title': x[0]})


		except:
			data = {'status': 'Error: unable to fecth data'}

		return data




	# gRecipeDetais - by id
	def gRecipeDetails(self):

		data = {}
		recipe = "SELECT Recipe.title, Recipe.description, Recipe.instructions, Recipe.image_link, Recipe.visible, Nutrition.calories, Nutrition.carbs, Nutrition.fat, Nutrition.protein, Nutrition.fiber FROM Recipe, Nutrition WHERE Recipe.id_nutrition = Nutrition.id_nutrition and Recipe.id_recipe = {}".format(self.args.get('id_recipe'))
		ing = "SELECT Ingredients.id_ingredient, Ingredients.nome_ingredient, Ingredients.calories, Ingredients.type, Ingredientes_Receita.amount FROM Ingredients, Ingredientes_Receita WHERE Ingredientes_Receita.id_ingredient = Ingredients.id_ingredient and Ingredientes_Receita.id_recipe = {}".format(self.args.get('id_recipe'))

		if not self.args.get('id_recipe'):
			data = {'status': 300, 'Message': 'parameter required [id_recipe]'}
		else:
			try:
				self.cursor.execute(recipe)
				recipes = self.cursor.fetchone()

				self.cursor.execute(ing)
				recipes_ing = self.cursor.fetchall()

				data = {'recipe': [{'id': self.args.get('id_recipe'), 'title': recipes[0], 'description': recipes[1], 'instructions': recipes[2], 'image_link': recipes[3], 'public': recipes[4], 'calories': recipes[5], 'fat': recipes[6], 'protein': recipes[7], 'fiber': recipes[8]}, {'ingredients': []}]}

				for y in recipes_ing:
					data['recipe'][1]['ingredients'].append({'id_ingredient': y[0], 'name': y[1], 'ingredient_calories': y[2], 'type': y[3], 'amount': y[4]})

			except:
				self.db.rollback()

		return data



	
	# get random recipe
	def gRandomRecipes(self, recipes):
		
		return recipes['results'][random.randint(0, len(recipes) - 1)]			





	# POST|UPDATE|DELETE REQUESTS
	# cRecipe - create recipe
	def cRecipe(self):
		
		if self.checkParam(['title', 'amount', 'instructions', 'id']) is False or len(self.args['id']) != len(self.args['amount']):
			return {'status': 'Error', 'Message':'Params Required [title, ingredients, instructions]'}
		
		try: calories = self.args['calories']
		except: calories = 0

		try: carbs = self.args['carbs']
		except: carbs = 0

		try: fat = self.args['fat']
		except: fat = 0

		try: protein = self.args['protein']
		except: protein = 0

		try: fiber = self.args['fiber']
		except: fiber = 0
		
		try: img_link = self.args['url_image']
		except: img_link = "-"
		
		try: desc = self.args['description']
		except: desc = "-"

		try: visible = self.args['visible']
		except: visible = 1
		
		#verify if ing_id exists
		for x in self.args['id']:
			if self.db_ver('Ingredients', 'id_ingredient', x) == 0:
				return {'status': 'ERROR', 'Message': 'ingredient doesnt exist in our database'}
		
		cRN = "INSERT INTO Nutrition (calories, carbs, fat, protein, fiber) VALUES ({}, {}, {}, {}, {})".format(calories, carbs, fat, protein, fiber)
		try:
			self.cursor.execute(cRN)
			nutrition_id = self.cursor.lastrowid

			cRecipeSql = "INSERT INTO Recipe (id_nutrition, title, description, instructions, image_link, image_type, created_at, id_user, updated_at, visible )VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', {})".format(nutrition_id, self.args['title'], desc, self.args['instructions'], img_link, 'jpg', datetime.date.today(), self.user_id, '0000-00-00', visible)
			
			self.cursor.execute(cRecipeSql)
			recipe_id = self.cursor.lastrowid
			
			for x in range(len(self.args['id'])):
				self.cursor.execute("INSERT INTO Ingredientes_Receita (id_ingredient, id_recipe, amount, id_amount_type) VALUES({}, {}, {}, {})".format(self.args['id'][x], recipe_id, self.args['amount'][x], '3'))
		
			self.db.commit()
			return {'status': 200, 'Message': 'Recipe Created [recipe_id = {}]'.format(recipe_id)}
		
		except:
			self.db.rollback()


		return {'status': 'ERROR', 'Message': 'Check your required parameters'}



	# uRecipe - update recipe
	def uRecipe(self, recipe_id):
		if self.db_ver('Recipe', 'id_recipe', recipe_id) == 0:		
			return {'Status':'ERROR', 'Message': 'Recipe id doesnt exist in our DB'}

		recipeFields = ['title', 'instructions', 'description', 'image_link', 'visible']
		nutritionFields = ['calories', 'fat', 'carbs', 'protein', 'fiber']	
	
		for x in recipeFields:
			if x in self.args:
				sql = "UPDATE Recipe SET {} = '{}', updated_at = '{}'  WHERE id_recipe = {} and id_user = {}".format(x, self.args[x], datetime.date.today(), recipe_id, self.user_id)
				self.cursor.execute(sql)				
			
		gNutritionId = "SELECT id_nutrition FROM Recipe WHERE id_recipe = {}".format(recipe_id)
		self.cursor.execute(gNutritionId)		
		nutrition_id = self.cursor.fetchone()[0]
		
		for x in nutritionFields:
			if x in self.args:
				sql = "UPDATE Nutrition SET {} = '{}' WHERE id_nutrition = {} ".format(x, self.args[x], nutrition_id)
				self.cursor.execute(sql)

		if 'id_ingredients' in self.args:
			for x in range(len(self.args['id_ingredients'])):
				sql = "UPDATE Ingredientes_Receita SET amount = {} WHERE id_recipe = {} and id_ingredient = {}".format(self.args['amount'][x], recipe_id, self.args['id_ingredients'][x])
				self.cursor.execute(sql)				

		self.db.commit()	
		return {"Status": 200, "Message":"Recipe Updated ['recipe_id': {}, 'updated_at': {} ]".format(recipe_id, datetime.date.today())}



	# dRecipe - delete recipe
	def dRecipe(self, recipe_id):
		
		if self.db_ver('Recipe', 'id_recipe', recipe_id) == 0:		
			return {'Status':'ERROR', 'Message': 'Recipe id doesnt exist in our DB'}

		sqlDRecipe = "DELETE FROM Recipe WHERE id_recipe = %s and id_user = %s"
		sqlDIngredients = "DELETE FROM Ingredientes_Receita WHERE id_recipe = %s"	
		
		# get nutrition_id
		gNutritionId = "SELECT id_nutrition FROM Recipe WHERE id_recipe = {}".format(recipe_id)
		self.cursor.execute(gNutritionId)		
		nutrition_id = self.cursor.fetchone()[0]
		
		# delete from table Nutrition
		sqlDNutrition = "DELETE FROM Nutrition WHERE id_nutrition = {}".format(nutrition_id)

		try:
			self.cursor.execute(sqlDIngredients, [recipe_id, self.user_id])	
			self.cursor.execute(sqlDRecipe, recipe_id)	
			self.cursor.execute(sqlDNutrition)
			
			self.db.commit()

		except:
			self.db.rollback()			

		return {'Status': 204, 'Message': 'Successful Deleted'}

		


	def __del__(self):
		"""
		Destroy the class recipes

		"""
		print("destroy class Recipes")
