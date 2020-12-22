import pymysql
import datetime

db = pymysql.connect("localhost","root","","quickrecipes")
cursor = db.cursor()

# INSERT EXAMPLE
# sql = "INSERT INTO Users (name,email, created_at, api_key) VALUES('teste','teste@teste.pt','{}','0000-0000-0000-0000')".format(datetime.date.today())
# try:
# 	cursor.execute(sql)
# 	db.commit()
#
# except:
# 	db.rollback()
# db.close()
