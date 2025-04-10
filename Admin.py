# import mysql.connector as msl
# mc=msl.connect(host="localhost",user="root",password="kaif",database="python_test")

                


# class Admin:
    
#     def add_admin(self):
#         cur=mc.cursor()
#         username = input("Enter Your Username : ") .strip()
#         password = input("Enter Your Password : ").strip()
#         cur.execute("insert into admin (username,password) values(%s,%s)",(username,password))
#         mc.commit()
#         cur.close()
#         return "Data Saved"
#     def Create_Table(self):
#         cur = mc.cursor()
#         cur.execute("CREATE TABLE IF NOT EXISTS Saving_Db(Account_no bigint primary key auto_increment,holder_name varchar(40) not null,Father_name varchar(40) not null,amount bigint check (amount>=500),dob date not null,age int not null,gender varchar(10) not null,email varchar(40) unique,phone bigint not null,atm_no bigint unique,atm_pin int unique,addresh varchar(255) not null)")
#         mc.commit()
#         return "Table Created Succesfully !!!" 
#     def show_admin(self):
#         cur=mc.cursor()
#         cur.execute("select * from admin")
#         print("\tUsername \t Password")
#         print("\t--------\t--------")
#         for d in cur:
#             print("\t",d[0],"\t",d[1])
#             print("\t------------------------")
#         cur.close()
#     def check_login(self):
#         cur=mc.cursor()
#         username = input("Enter Your Username : ") .strip()
#         password = input("Enter Your Password : ").strip()
#         cur.execute("select  *from admin where username=%s and password=%s",(username,password))
#         for d in cur:
#             if username in d and password in d:
#                 pass
        
        
# obj =Admin()        
# while(1):
#     ch=int(input("\t----------------------\n \t  What You Want !!!\n \t----------------------\n \t 1 ) Check All Admins \n\t----------------------\n \t 2 ) Create Tables \n\t----------------------\n \t 3 ) Add Admin \n\t----------------------\n \t => Choice : "))
#     match(ch):
#             case 1:
#                 obj.show_admin()
#                 break
#             case 2:
#                 obj.Create_Table()
#             case 3:
#                 obj.add_admin()
#             case defaul:
#                 print("Invalid Option")
    

# # obj.check_login()
# # obj.Create_Table() 
# # print(obj.add_admin())


# # 

    
    
