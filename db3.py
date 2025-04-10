import  mysql.connector as msl
dbs=msl.connect(host="localhost",user="root",password="kaif",database="p1_db")
mr=dbs.cursor()
#mr.execute("create database p1_db")
#mr.execute("create table accountInfo(ac_no int primary key)")
#mr.execute("alter table accountInfo modify ac_no int  ")
#mr.execute("alter table accountInfo add column (email varchar(30) unique not null)")
mr.execute("desc accountinfo")
for db in mr:
    for d in db:
      print(d,end="\t")
    print()
print("successfully")
dbs.commit()
print("successfully")
