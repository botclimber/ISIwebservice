
# params:
#	- results
#	- minfiber
#	- cals
#	- protein
#	- fat
#	- carbs
#	- sort
#	- sortDirection	(asc or desc)

class Recipes:

	def __init__(self, db, userId, args ):

		self.db = db
		self.cursor = db.cursor()

		self.user_id = int(userId)
		self.args = args

	# method that returns recipes
	def gRecipes(self):
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

			data = {'results': [],'nr_results': len(results) }
			for x in results:
				data['results'].append({'id': x[1],'calories': x[3], 'carbs': x[4], 'fat': x[5], 'protein': x[6], 'fiber': x[7], 'image': x[2], 'imageType': 'jpg,jpeg', 'title': x[0]})


		except:
			data = {'status':'Error: unable to fecth data'}

		return data

	# gRecipeByIng
	# gRecipeDetais - by id
	# gRandomRecipe

	# cRecipe - create recipe
	# uRecipe - update recipe
	# dRecipe - delete recipe

	def __del__(self):
		print("detroy class Recipes")
