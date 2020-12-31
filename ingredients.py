

class Ingredients:

	def __init__(self, db, user_id = 0, args = []):
		
		self.db = db
		self.cursor = db.cursor()
		
		self.args = args
		self.user_id = int(user_id)


	def gIngredients(self):
		sql = "SELECT * FROM Ingredients "

		sql += "WHERE nome_ingredient LIKE '{}%' ".format(self.args.get('name')) if self.args.get('name') != None else ""
		sql += "LIMIT {}".self.args.get('results') if self.args.get('results') != None else ""

		try:
			self.cursor.execute(sql)
			content = self.cursor.fetchall()
	
			data = {'content': [], 'nr_results': len(content)}
			for x in content:
				data['content'].append({'id': x[0], 'name': x[2], 'type': x[5]})

		except:
			data = {'status': 'Error: unable to fetch data'}	

		return data		

	def gIngredientDetails(self):
		
		if self.args.get('ingredient_id') == None:
			return {'status': 300, 'Message':'parameter required [ingredient_id]'}
		
		data = {'content':[], 'total_results': 0}
		for x in self.args.get('ingredient_id').split(','):
			x = int(x)			
	
			ingredient = "SELECT * FROM Ingredients WHERE id_ingredient = {}".format(x)
			recipes = "SELECT Recipe.id_recipe, title, description, image_link FROM Recipe, Ingredientes_Receita WHERE Ingredientes_Receita.id_ingredient = {} and Ingredientes_Receita.id_recipe = Recipe.id_recipe and (Recipe.visible = 1 or (Recipe.visible = 0 and Recipe.id_user = {}))".format(x, self.user_id)

			try:
				self.cursor.execute(ingredient)
				ing = self.cursor.fetchone()			
			
				if self.cursor.rowcount > 0:
					data['content'].append({'recipes':[], 'ingredient':{'id': ing[0], 'name': ing[2], 'calories': ing[3], 'type': ing[5], 'created_at': ing[4] }})
				
					if self.args.get('lite') != None and int(self.args.get('lite')) == 1:
						self.cursor.execute(recipes)
						recipesContent = self.cursor.fetchall()
					
						if len(recipesContent) > 0:
							for i in recipesContent:
								data['content'][len(data['content'])-1]['recipes'].append({'recipe_id': i[0], 'title': i[1], 'description': i[2], 'image_link': i[3]})			
				
					data['total_results'] += 1
			except:	
				data = {'Status': 301, 'Message': 'unable to fetch data'}
	
		return data


	def cIngredient(self):
		pass	

	def uIngredient(self, ing_id):
		pass

	def dIngredient(self, ing_id):
		pass
