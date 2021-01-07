
class Security:

	def __init__(self, db):
		"""
		Constructor of this object
		:param db: variable object of database
		"""
		self.db = db
		self.cursor = db.cursor()


	def gUserId(self, apiKey):
		"""
		Get user id by apikey

		:param apiKey: apikey to found in database
		:type apiKey: strign
		:return: array with the result
		"""
		sql = "SELECT id_user FROM Users WHERE api_key = '{}'".format(apiKey)
		
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()

		except:
			self.db.rollback()

		return result[0][0]
