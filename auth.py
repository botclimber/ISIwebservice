import secrets
import datetime

# Auth Managment
class Auth:
	
	def __init__ (self, name, email, db):
		self.name = name
		self.email = email
		self.db = db
		self.cursor = db.cursor()

	def cApiKey(self):
		return secrets.token_urlsafe(10)			

	def cUser(self, key):
		sql = "INSERT INTO Users(name,email,created_at,api_key)VALUES('{}','{}','{}','{}')".format(self.name, self.email, datetime.date.today(),key)
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			
			return 200
		except:
			self.db.rollback()
			return 201
		
	def __del__(self):
		print("destroy class Auth")	
