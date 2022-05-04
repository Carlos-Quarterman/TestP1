from ast import And, For
import collections
import select
from unittest import result
import pymongo
from pymongo import mongo_client
import json

myclient = pymongo.MongoClient("127.0.0.1", 27017) 
db = myclient.Project1
collections = myclient.account

with open('account.json') as a1:
  file_data = json.load(a1)

class BankingAppilication :

 FirstName = ""
 LastName = ""
 AccountNumC = ""
 AccountNumS = ""
 BalanceC = ""
 BalanceS = ""
 
# Update Balance
def Deposit():
 amount = input("Enter amount to be deposit")
 print("Amount Desposit: ", amount)
 file_data.BalanceC = file_data.BalanceC + amount
print("Balance: ", file_data.BalanceC)


#delete 
def Withdraw():
 amount = input("Enter amount to be deposit")
 print("Amount Desposit: ", amount)
 file_data.BalanceC = file_data.BalanceC - amount
print("Balance: ", file_data.BalanceC)


#Reading Account
def Checking():
  AccountNumC = int(input("Enter Checking Account Number: "))
  file_data.collection.find(AccountNumC) 
  if AccountNumC == file_data.collection.find() :
   print(file_data.FirstName)
   print(file_data.LastName)
   print("Checking Account Number:" , AccountNumC)
   print("Balance:" " ${:,.2f}".format(file_data.BalanceC))
 #elif AccountNumC == 5475806426 :
  #print("First Name: " 'Erica')
  #print("Last Name: " 'Johnson')
  #print("Checking Account Number:" , AccountNumC)
  #print("Balance:" " ${:,.2f}".format(3940.86))
 #elif AccountNumC == 5475835453 :
  #print("First Name: " 'Kim')
  #print("Last Name: " 'Thomas')
  #print("Account Number:" , AccountNumC)
  #print("Balance:" " ${:,.2f}".format(6764.32))
  else :
   print("Invalid")
#def Saving():
 #AccountNumS = int(input("Enter Saving Account Number: "))
 #file_data.collection.find({AccountNumS : ""}) 
 #if AccountNumS == 5475835231 :
  #print("First Name: " 'Tom')
  #print("Last Name: " 'Jones')
  #print("Saving Account Number:" , AccountNumS)
  #print("Balance:" " $ {:,.2f}".format(500876.89))
 #elif AccountNumS == 5475806427 :
  #print("First Name: " 'Erica')
  #print("Last Name: " 'Johnson')
  #print("Saving Account Number:", AccountNumS)
  #print("Balance:" " ${:,.2f}".format(4087.89))
 #elif AccountNumS == 5475835454 :
  #print("First Name: " 'Kim')
  #print("Last Name: " 'Thomas')
  #print("Saving Account Number:", AccountNumS)
  #print("Balance:" " $ {:,.2f}".format(90343.04))
 #else :
  #print("Invalid")

def DisplayAll():
    FirstName = input("Enter First Name: ")
    file_data.collection.find(FirstName)
    LastName = input("Enter Last Name: ")
    file_data.collection.find(FirstName)
   # account.find({FirstName : ''})
   # account.find({LastName : ''}) 
    if FirstName and LastName  :
     print(FirstName)
     print(LastName)
     print("Checking Account Number: ", file_data.collection.find.AccountNumC)
     print("Checking Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceC))
     print("Saving Account Number: ", file_data.collection.find.BalanceS)
     print("Saving Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceS))
    elif FirstName  and LastName :
     print(FirstName)
     print(LastName)
     print("Checking Account Number: ", file_data.collection.find.AccountNumC)
     print("Checking Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceC))
     print("Saving Account Number: ", file_data.collection.find.AccountNumS)
     print("Saving Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceS))
    elif FirstName and LastName :
     print(FirstName)
     print(LastName)
     print("Checking Account Number: ", file_data.collection.find.AccountNumC)
     print("Checking Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceC))
     print("Saving Account Number: ", file_data.collection.find.AccountNumS)
     print("Saving Account Balance:" " ${:,.2f}".format(file_data.collection.find.BalanceS))
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

while BC != 5:

   print("\tMain Menu")

   print("\t1. Checking Account")

   #print("\t2. Savings Account")

   print("\t2. Deposit")

   print("\t3. Withdown")

   print("\t4. Display Account Information")

   print("\t5. Exit")

   print("\tSelect Your Option (1-6): ")

   BC = input()

   if BC == '1':

     Checking()
     
   #elif BC =='2':

     #Saving()

   elif BC == '2':

     Deposit()

   elif BC == '3':

     Withdraw()

   elif BC == '4':

     DisplayAll()

   elif BC == '5':

       print("\tThanks for using Apple Banking System")

       break

   else :

       print("Invalid selection")  

       BC = input("Enter your choice : ")

