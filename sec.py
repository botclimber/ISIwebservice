
class Security:

	def __init__(self, db):
		self.db = db
		self.cursor = db.cursor()

	def verify(self, field, value):
		# verifys if apiKey exists in db
		sql = "SELECT name FROM Users WHERE {} = '{}' ".format(field, value)
		
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()

			
		except:
			db.rollback()			

		return True if len(result) == 1 else False

	def gUserId(self, apiKey):
		sql = "SELECT id_user FROM Users WHERE api_key = '{}'".format(apiKey)
		
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()

		except:
			db.rollback()

		return result[0][0]
