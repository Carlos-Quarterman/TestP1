from ast import And, For
import select
from unittest import result
import pymongo
from pymongo import mongo_client

client = pymongo.MongoClient("127.0.0.1", 27017) 
db = client.Project1
collection = db.account

class BankingAppilication :

 FirstName = ""
 LastName = ""
 AccountNumC = ""
 AccountNumS = ""
 BalanceC1 = ""
 BalanceS1 = ""
 
def Checking():
 AccountNumC = int(input("Enter Checking Account Number: "))
 collection.find({AccountNumC : ""}) 
 if AccountNumC == 5475835230 :
  print("First Name: " 'Tom')
  print("Last Name: " 'Jones')
  print("Checking Account Number:" , AccountNumC)
  print("Balance:" " ${:,.2f}".format(1900.86))
 elif AccountNumC == 5475806426 :
  print("First Name: " 'Erica')
  print("Last Name: " 'Johnson')
  print("Checking Account Number:" , AccountNumC)
  print("Balance:" " ${:,.2f}".format(3940.86))
 elif AccountNumC == 5475835453 :
  print("First Name: " 'Kim')
  print("Last Name: " 'Thomas')
  print("Account Number:" , AccountNumC)
  print("Balance:" " ${:,.2f}".format(6764.32))
 else :
  print("Invalid")
def Saving():
 AccountNumS = int(input("Enter Saving Account Number: "))
 collection.find({AccountNumS : ""}) 
 if AccountNumS == 5475835231 :
  print("First Name: " 'Tom')
  print("Last Name: " 'Jones')
  print("Saving Account Number:" , AccountNumS)
  print("Balance:" " $ {:,.2f}".format(500876.89))
 elif AccountNumS == 5475806427 :
  print("First Name: " 'Erica')
  print("Last Name: " 'Johnson')
  print("Saving Account Number:", AccountNumS)
  print("Balance:" " ${:,.2f}".format(4087.89))
 elif AccountNumS == 5475835454 :
  print("First Name: " 'Kim')
  print("Last Name: " 'Thomas')
  print("Saving Account Number:", AccountNumS)
  print("Balance:" " $ {:,.2f}".format(90343.04))
 else :
  print("Invalid")

def DisplayAll():
    FirstName = input("Enter First Name: ")
    LastName = input("Enter Last Name: ")
    collection.find({FirstName : ''})
    collection.find({LastName : ''}) 
    if FirstName == 'Tom' and LastName == 'Jones' :
     print(FirstName)
     print(LastName)
     print("Checking Account Number: " '5475835230')
     print("Checking Account Balance:" " ${:,.2f}".format(1900.86))
     print("Saving Account Number: " '5475835231')
     print("Saving Account Balance:" " ${:,.2f}".format(500876.89))
    elif FirstName == 'Erica' and LastName == 'Johnson':
     print(FirstName)
     print(LastName)
     print("Checking Account Number: " '5475806426')
     print("Checking Account Balance:" " ${:,.2f}".format(3940.86))
     print("Saving Account Number: " '5475806427')
     print("Saving Account Balance:" " ${:,.2f}".format(4087.89))
    elif FirstName == 'Kim' and LastName == 'Thomas':
     print(FirstName)
     print(LastName)
     print("Checking Account Number: " '5475835453')
     print("Checking Account Balance:" " ${:,.2f}".format(6764.32))
     print("Saving Account Number: " '5475835454')
     print("Saving Account Balance:" " ${:,.2f}".format(90343.04))
    else :
       print("Invalid")

#Introduction of the Banking Application

def Intro():

   print("\t\t\t\t**********************")

   print("\t\t\t\t*APPLE ONLINE BANKING*")

   print("\t\t\t\t**********************")

   #input()

# start of the program

BC = " "

num = 0

Intro()

while BC != 4:

   print("\tMain Menu")

   print("\t1. Checking Account")

   print("\t2. Savings Account")

   print("\t3. Display Account Information")

   print("\t4. Exit")

   print("\tSelect Your Option (1-4): ")

   BC = input()

   if BC == '1':

     Checking()
     
   elif BC =='2':

     Saving()

   elif BC == '3':

     DisplayAll()

   elif BC == '4':

       print("\tThanks for using Apple Banking System")

       break

   else :

       print("Invalid selection")  

       BC = input("Enter your choice : ")

