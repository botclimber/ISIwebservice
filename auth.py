import secrets
import datetime

# Auth Managment
class Auth:
	
	def __init__ (self, name, email, db):
		"""
			Constructor of this object
			:param name: user name
			:param email: user email
			:param db: variable object of database
			:type name: string
			:type email: string
		"""
		self.name = name
		self.email = email
		self.db = db
		self.cursor = db.cursor()

	def cApiKey(self):
		"""
		Creat ApiKey

		:param self: object with the all information for generate the apikey
		:type self: object

		:return: a string with the user apikey
		"""
		return secrets.token_urlsafe(10)			

	def cUser(self, key):
		"""
		Creat and insert a new user in database

		:param self: object with all information about the new user
		:param key: the apikey for this user
		:type self: object
		:type key: string
		:return 200: if was insert with success
		:return 201: if wasn't insert with success
		"""
		sql = "INSERT INTO Users(name,email,created_at,api_key)VALUES('{}','{}','{}','{}')".format(self.name, self.email, datetime.date.today(),key)
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			
			return 200
		except:
			self.db.rollback()
			return 201
		
	def __del__(self):
		"""
		destoy this class
		"""
		print("destroy class Auth")	
