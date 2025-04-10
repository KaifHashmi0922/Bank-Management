import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='kaif',database='Python_test')
# print(list(db))
cur=db.cursor()
cur.execute("select *from test")
print([ i  for i in cur ])