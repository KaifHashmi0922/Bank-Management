import mysql.connector as msl
#from Atm import gen_pin,cng_pin,reset_pin
#mc=msl.connect(host="localhost",user="root",password="kaif",database="bank_management")
email_check=['.com','.in']
# s=["1st","2nd","3rd"]
class AccountNotFoundError(Exception):
    def __init__(self,msg):
        self.msg=msg
class InsufficientBalnceError(Exception):
    def __init__(self,msg):
        self.msg=msg
class PinInValidError(Exception):
    def __init__(self,msg,i):
        self.msg=msg
        print(s[i],"Attempt Is Fail")
class PinInValidErrors(Exception):
    def __init__(self,msg):
        self.msg=msg

"""
def  create_account():
try:
    e_check=[]
    ad_check=[]
    ca=mc.cursor()
    ca.execute("select adhar_no,email from Saving_DB")
    for data in ca:
        e_check.append(data[0])
        ad_check.append(data[1])
    while True:
        name=input("  \t\t\t\t\t\tEnter Your Name  :  ").strip()
        fname=input("  \t\t\t\t\t\tEnter Your Father Name  :  ").strip()
        adno=input("  \t\t\t\t\t\tEnter Adhar No   :  ").strip()
        email=input("  \t\t\t\t\t\tEnter Your Email  :  ").strip()
        if adno.isdigit() and len(adno)==12 and adno not in ad_check :
            if email not in e_check:
                amt=int(input("  \t\t\t\t\t\tEnter The Balance   :  "))
            else:
                raise
        else:
            raise InvalidAdharNoError("Invalid Adhar No !!!")
except:
    pass
            print("  \t\t\t\t\t\tPls Enter Correct Adhar No  !!!")
    cr=mc.cursor()
    cr.execute
    cr.close()
"""
def withdraw():
        cur=mc.cursor()
        while True :
            try:
                 r=[]
                 cur.execute("select ac_no from  Saving_DB ")
                 for d in cur:
                     for data in d:
                         r.append(data)
                 acno=input("  \t\t\t\t\t\tEnter Account No  :  ").strip()
                 if acno.isdigit() and int(acno) in r:
                     cur.execute("select amount,atm_pin from  Saving_DB where ac_no=%s",(acno,))
                     k=cur.fetchall()
                     am=k[0][0]
                     p=k[0][1]
                     wam=input("  \t\t\t\t\t\tEnter Amount To Withdraw").strip()
                     if wam.isdigit() and int(wam)<=am:
                        c=3
                        while c>0:
                            wpin=input("  \t\t\t\t\t\tEnter The Pin  :  ").strip()
                            if wpin.isdigit() and int(wpin)==p:
                                 cur.execute("update Saving_DB set amount=amount-%s where ac_no=%s",(wam,acno))
                                 mc.commit()
                                 print("  \t\t\t\t\t\tTransction Is Completed Succesfully  !!!")
                                 cur.close()
                                 w1=input("  \t\t\t\t\t\tQ)  Do You Want To  Continue Operation   :   ( Y  /  N )")
                                 if w1.lower()=="n":
                                     break
                                 elif w.lower()=="exit":
                                     exit()
                            else:
                                 raise PinInValidErrors("  \t\t\t\t\t\tInvalid Pin")
                                 c=c-1
                                 
                     else:
                         raise InsufficientBalnceError("  \t\t\t\t\t\tInsufficient Balance")
                         
                 else:
                     raise AccountNotFoundError("  \t\t\t\t\t\tAccount Does'not Exists")
                     
            except AccountNotFoundError as msg :
                print(msg)
                break
            except InsufficientBalnceError as msg :
                print(msg)
                break
            except PinInValidErrors as msg :
                print(msg)
          #  except  ManyTimesWrong as msg :
            #    print(msg)
           #     break
                
def fund_trans(self):
    dp=mc.cursor()
    dp.execute("select ac_no,amount,atm_pin from Saving_DB")
    a=[]
    for data in dp:
        a.append(data[0])
    try:
        while True:
            sacno=int(input("  \t\t\t\t\t\tEnter  Source Account No  :  "))
            if sacno in a:
               dacno=int(input("  \t\t\t\t\t\tEnter Destination Account No  :  "))
               if dacno in a:
                       amt=int(input("  \t\t\t\t\t\tEnter Amount To Fund Transfer   :   "))
                       spin=int(input("  \t\t\t\t\t\tEnter Pin"))
                       dp.execute("select amount,atm_pin from Saving_DB where ac_no=%s",(sacno,))
                       for d in dp:
                           cbal=d[0]
                           vpin=d[1]               
                       if amt<=cbal:
                           if spin==vpin:
                               dp.execute("update Saving_DB set amount=amount-%s where ac_no=%s",(amt,sacno))
                               dp.execute("update Saving_DB set amount=amount+%s where ac_no=%s",(amt,dacno))
                               mc.commit()
                               print("  \t\t\t\t\t\tFund Transfer  Is Succesfully  !!!")
                                
                           else:
                               raise PinInValidError ("  \t\t\t\t\t\tPls Re-Enter  You Pin !!!")
                       else:
                           raise InsufficientBalnceError("  \t\t\t\t\t\tInsufficient Amount Pls Enter Sufficient Amount  !!!!")
               else:
                   raise  AccountNotFoundError("  \t\t\t\t\t\tThis ",dacno,"Does't Exists  !!")
            else:
                raise AccountNotFoundError("  \t\t\t\t\t\tThis ",sacno,"Does't Exists  !!")
    except AccountNotFoundError as msg:
            print(msg)
    except AccountNotFoundError as msg:
            print(msg)
    except InsufficientBalnceError as msg :
            print(msg)
    except  PinInValidErrors as msg :
            print(msg)
            rollback()
        
def check_bal():
    print("\n","~"*113)
    a=[]
    cur=mc.cursor()
    cur.execute("select ac_no from Saving_DB")
    r=cur.fetchall()
    for data in r:
        for d in data:
            a.append(d)
    print(a)
    try:
        while True:
            eacno=input("  \t\t\t\t\t\tEnter Account NO  :  ").strip()
            if int(eacno) in a:
                c=3
                cur.execute("select atm_pin,amount from Saving_DB where ac_no=%s ",(eacno,))
                r=cur.fetchall()
                for d in r:
                    p=d[0]
                    am=d[1]
                print(p,am)
                while c>0:
                   c-=1
                   epin=input("  \t\t\t\t\t\tEnter Your Pin  :  ").strip()
                   if epin.isdigit() and int(epin)==p:
                       print("  \t\t\t\t\t\t","~"*33)
                       print("   \t\t\t\t\t\tYour Current Balance Is :\t", am)
                       print("  \t\t\t\t\t\t","~"*33)
                       w=input("  \t\t\t\t\t\tQ)  Do You Want To  Continue Operation   :   ( Y  /  N )")
                       if w.lower()=="n":
                           break
                       elif w.lower()=="exit":
                           exit()
                   else:
                       print("\t\t\t\t\t\t",s[2-c],"Attmep Faild  !!!  ")
                       if c==0:
                          raise PinInValidError2("  \t\t\t\t\t\tYou Enterd  Wrong Pin Many Times !!! ")
                          break
            else:
                 raise AccountNotFoundError("  \t\t\t\t\t\tAccount Does'not Exists")
    except  AccountNotFoundError as msg :
        print(msg)
    except PinInValidError2 as msg :
        print(msg)
        
# comp
def display_single():
    a=[]
    n=[]
    while True:
        try:
            print("\n","~"*130)
            cur=mc.cursor()
            cur.execute("select ac_no,ac_h_name from Saving_DB")
            r=cur.fetchall()
            for data in r:
                a.append(data[0])
                n.append(data[1])
            eacno=input("  \t\t\t\t\t\tEnter Account No   :   ").strip()
            ename=input("  \t\t\t\t\t\tEnter Account Holder Name  :   ").strip()
            if eacno.isdigit() and int(eacno) in a and ename in n:
                cur.execute("select *from Saving_DB where ac_no=%s and  ac_h_name=%s",(eacno,ename))
                print("~"*113)
                print("ACCOUNT NO | HOLDER NAME | FATHER NAME | AMOUNT | DOB | AGE | GENDER | EMAIL |  PHONE  |  ATM NO  |  ATM PIN  | ADDRESH | ")
                print("~"*113)
                d=list(cur)[0]
                for data in d:
                    print(" ",data,end="   ")
                print("","~"*112)
                w=input("  \t\t\t\t\t\tQ)  Do You Want To  Continue Operation   :   ( Y  /  N )   :   ")
                if w.lower()=="n":
                    break
                elif w.lower()=="exit":
                    exit()

            else:
                raise  AccountNotFoundError("\t\t\t\t\t\tAccount Does'not Exists")
        except  AccountNotFoundError as msg :
            print(msg)
            w=input("  \t\t\t\t\t\tQ)  Do You Want To  Continue Operation   :   ( Y  /  N ) And ( Exit )   :   ")
            if w.lower()=="n":
                    break
            elif w.lower()=="exit":
                exit()
        finally:
            cur.close()
def display_all():
    s1=[]
    cur=mc.cursor()
    cur.execute("select *from Saving_DB")
    print("~"*113)
    print(" ACCOUNT NO | HOLDER NAME | FATHER NAME | AMOUNT | DOB | AGE | GENDER | EMAIL |  PHONE  |  ATM NO  |  ATM PIN  | ADDRESH | ")
    print("\n","~"*113)
    for data  in cur:
        for d in data:
            print("    ",d,"    |",end="")
        print("\n","~"*113)
    cur.close()
def atm_pin_operation():
    while True:
        ca=input("  \t\t\t\t\t\t1) GENRATE PIN  :  \n  \t\t\t\t\t\t2) CHANGE PIN  : \n  \t\t\t\t\t\t3) RESET PIN  : \n  \t\t\t\t\t\tQ) ENTER CHOICE  :  ")
        if ca=='1' or ca.lower()=='one':
            gen_pin()
        elif ca=='2' or ca.lower()=='two':
            cng_pin()
        elif ca=='3' or ca.lower()=='three':
            reset_pin()
        else:
           print("  \t\t\t\t\t\tPls Enter Valid No")
def close_account():
    pass
def show():
    
    print("\t"*5,"~"*44)
    print("\t"*5,"**  SAVEING  ACCOUNT   DEPARTMENT  **")
    print("\t"*5,"~"*44)
    print(""*6,"~"*113)
    while True:
        ch=input("  \t\t\t\t\t\t1)Create Account  : \n  \t\t\t\t\t\t2) Deposite  : \n  \t\t\t\t\t\t3) Withdraw  : \n  \t\t\t\t\t\t4) Fund Transfer  : \n  \t\t\t\t\t\t5) Check Balance  :  \n  \t\t\t\t\t\t6) Display Single Customer   :  \n  \t\t\t\t\t\t7) Display All Customer  :  \n  \t\t\t\t\t\t8) Mini Statement  :\n  \t\t\t\t\t\t9) ATM Operation  :  \n \t\t\t\t\t\t10) Close Account  :\n  \t\t\t\t\t\t11) Department Exit  :  \n  \t\t\t\t\t\t12)  Application Exit  :  \n   \t\t\t\t\t\tQ) Enter Choice  : ")
        if ch.isdigit() :
            match int(ch):
                case 1:
                    create_account()
                case 2:
                    deposite()
                case 3:
                    withdraw()
                case 4:
                    fund_trans()
                case 5:
                    check_bal()
                case 6: 
                    display_single()
                case 7:
                    display_all()
                case 8:
                    mini_stmt()
                case 9:
                    atm_pin_operation()
                case 10:
                    close_account()
                case 11:
                    break
                case 12:
                    exit()
                case default :
                    print("  \t\t\t\t\t\tPls Enter valid choice")      
   
