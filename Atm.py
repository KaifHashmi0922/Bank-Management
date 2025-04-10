# # import mysql.connector as msl
# # mc=msl.connect(host="localhost",user="root",password="kaif",database="p1_db")

# def gen_pin():
#   try:
#     cur=mc.cursor()
#     cno=input("\t\t\t\t\t\tInsert Your Card  No !!").strip()
#     while True:
#     cur.execute("select phone from  where atm_no=%s",(cno,))
#     p_check=list(cur)[0][0]
#     pho=int(input("  \t\t\t\t\t\tEnter Your Bank Ragister No :  "))
#     if pho==p_check:
#       npin=input("  \t\t\t\t\t\tEnter 4 Digit  Pin  :  ").strip()
#       vpin=input("  \t\t\t\t\t\tRe-Enter  4 Digit Pin  :  ").strip()
#       if npin.isdigit() and vpin.isdigit() and len(npin)==4 and  len(vpin)==4:
#         if npin==vpin:
#           cur.execute("update Saving_DB set atm_pin=%s where atm_no=%s and phone=%s",(vpin,cno,pho))
#           mc.commit()
#           print("  \t\t\t\t\t\tYour Pin Genrated Successfully !!!")
#           print("  \t\t\t\t\t\t","~"*33)
#           print("  \t\t\t\t\t\tYour Pin Is  :  ",vpin)
#           print("  \t\t\t\t\t\t","~"*33)
#           ch=input("  \t\t\t\t\t\tDo You Wan't Continue  Operation !!").strip()
#           if ch.lower()=="n":
#             exit()
#           else:
#             break
#         else:
#           print("  \t\t\t\t\t\tBoth Pin Not Macthed  !!!")
#       else:
#         print("  \t\t\t\t\t\tPls Enter 4 Digit Numeric Pin  !!!")
#     else:
#       print("  \t\t\t\t\t\tPls Enter Correct Register No !!!")
# def cng_pin():
#   cno=int(input("  \t\t\t\t\t\tInsert Your Card No  :  "))#.strip()
#   cur=mc.cursor()
#   cur.execute("select atm_pin from Saving_DB where atm_no=%s",(cno,))
#   cp=list(cur)[0][0]
#   while True :
#     cpin=int(input("  \t\t\t\t\t\tEnter Your Current Pin  :  "))#.strip())
#     if cp==cpin:
#       npin=int(input("  \t\t\t\t\t\tEnter New Pin  :   "))#.strip()
#       vpin=int(input("  \t\t\t\t\t\tRe-Enter New Pin  :   "))#.strip()
#       if len(npin)==4 and len(vpin)==4:
#         if npin==vpin:
#           cur.execute("update Saving_DB set atm_pin=%s where atm_no=%s",(vpin,cno))
#           mc.commit()
#           print("  \t\t\t\t\t\tPin Change Successfully  !!!")
#           print("  \t\t\t\t\t\t","~"*33)
#           print("  \t\t\t\t\t\tYour Pin Change  :  ",vpin)
#           print("  \t\t\t\t\t\t","~"*33)
#           ch=input("  \t\t\t\t\t\tDo You Wan't Continue  Operation !!").strip()
#           if ch.lower()=="n":
#               exit()
#               cur.close()
#           else:
#               break
#         else:
#          print("  \t\t\t\t\t\tPls Enter Minimum 4 ( Four ) Digit Pin  !!!")
#       else:
#          print("  \t\t\t\t\t\tRe-Enter New Pin  !!!")
#     else:
#       print("  \t\t\t\t\t\tRe-Enter Current Pin !!! ")
# def reset_pin():
#       cno=int(input("  \t\t\t\t\t\tEnter You Card No  :   "))
#       cur=mc.cursor()
#       cur.execute("select atm_no,phone,adhar_no,atm_pin from Saving_DB where  atm_no=%s",(cno,))
#       for d in cur:
#         at_check=d[0]
#         p_check=d[1]
#         a_check=d[2]
#         ap_check=d[3]
#       if cno==at_check:
#         cho=input("  \t\t\t\t\t\t1) Backup Pin  :\n    \t\t\t\t\t\t2) Reset Pin  ")
#         if  cho=='1' or cho.lower()=='one':
#             while True:          
#              ph=input("  \t\t\t\t\t\tEnter Your Ragisterd Phone No  :   ").strip()
#              if ph.isdigit() and len(ph)==10 and int(ph)==p_check:
#                 ad=input("  \t\t\t\t\t\tEnter Your Adhar No  :  ").strip()
#                 if ad.isdigit() and len(ad)==12 and int(ad)==a_check :
#                     print("  \t\t\t\t\t\t","~"*33)
#                     print("  \t\t\t\t\t\tYour Pin  Current Pin  is   :   ",ap_check)
#                     print("  \t\t\t\t\t\t","~"*33)
#                     ch=input("  \t\t\t\t\t\tDo You Wan't Continue  Operation !!").strip()
#                     if ch.lower()=="n":
#                         exit()
#                         cur.close()
#                     else:
#                         break
#                 else:
#                     print("  \t\t\t\t\t\tAdhar No Is Invalid  \n  \t\t\t\t\t\tPls Enter Valid Adhar No  !!!")
#              else:
#                 print("  \t\t\t\t\t\tPhone No Is Invalid  \n  \t\t\t\t\t\tPls Enter Valid Phone No  !!!")
#         elif int(cho)==2 or cho.lower()=='two':
#              while True:
#                 ph=input("  \t\t\t\t\t\tEnter Your Ragisterd Phone No  :   ").strip()
#                 if ph.isdigit() and len(ph)==10 and int(ph)==p_check:
#                   ad=input("  \t\t\t\t\t\tEnter Your Adhar No  :  ").strip()
#                   if ad.isdigit() and len(ad)==12 and int(ad)==a_check :
#                      npin=input("  \t\t\t\t\t\tEnter New Pin  :  ").strip()
#                      vpin=input("  \t\t\t\t\t\tRe-Enter New Pin  :  ").strip()
#                      if  npin.isdigit() and vpin.isdigit() and len(npin)==4 and len(npin)==len(vpin) and  npin==vpin:
#                        cur.execute("update Saving_DB set atm_pin=%s where phone=%s and adhar_no=%s ",(vpin,ph,ad))
#                        mc.commit()
#                        print("  \t\t\t\t\t\tPin Reset Successfully  !!!")
#                        print("  \t\t\t\t\t\t","~"*33)
#                        print("Your Current Pin  :  ",vpin)
#                        print("  \t\t\t\t\t\t","~"*33)
#                        ch=input("Do You Wan't Continue  Operation !!").strip()
#                        if ch.lower()=="n":
#                            exit()
#                            cur.close()
#                        else:
#                            break
#                      else:
#                        print("Invalid Pin \n Pls Re_Enter Pin !!!")
#                   else:
#                      print("Adhar No Is Invalid \n Pls Enter Bank-Link Adhar  No  !!!")
#                 else:
#                   print("Phone No Is Invalid \n Pls Enter Valid Ragisterd Phone No  !!!")
#         else:
#             print("Invalid Choice")
#       else:
#          print("Your Card No Is Invalid  !!!")

# """
# while True:
#     ca=input("  \t\t\t\t\t\t1) GENRATE PIN  :  \n  \t\t\t\t\t\t2) CHANGE PIN  : \n  \t\t\t\t\t\t3) RESET PIN  : \n  \t\t\t\t\t\t Q) ENTER CHOICE  :  ")
#     if ca=='1' or ca.lower()=='one':
#         gen_pin(cur)
#     elif ca=='2' or ca.lower()=='two':
#         cng_pin(cur)
#     elif ca=='3' or ca.lower()=='three':
#         reset_pin(cur)
#     else:
#         print("pls Enter Valid No")

# """
