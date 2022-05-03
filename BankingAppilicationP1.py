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
  print({"FirstName": 'Tom'})
  print({"Lastname": 'Jones'})
  print({"AccountNumC": 5475835230})
  print({"BalanceC": 1900.86})
 elif AccountNumC == 5475806426 :
  print({"FirstName": 'Erica'})
  print({"Lastname": 'Johnson'})
  print({"AccountNumC": 5475806426})
  print({"BalanceC": 3940.86})
 elif AccountNumC == 5475835453 :
  print({"FirstName": 'Kim'})
  print({"Lastname": 'Thomas'})
  print({"AccountNumC": 5475835453})
  print({"BalanceC": 6764.32})
 else :
  print("Invalid")

def Saving():
 AccountNumS = int(input("Enter Saving Account Number: "))
 collection.find({AccountNumS : ""}) 
 if AccountNumS == 5475835231 :
  print({"FirstName": 'Tom'})
  print({"Lastname": 'Jones'})
  print({"AccountNumS": 5475835231})
  print({"BalanceS": 500876.89})
 elif AccountNumS == 5475806427 :
  print({"FirstName": 'Erica'})
  print({"Lastname": 'Johnson'})
  print({"AccountNumS": 5475806427})
  print({"BalanceS": 4087.89})
 elif AccountNumS == 5475835454 :
  print({"FirstName": 'Kim'})
  print({"Lastname": 'Thomas'})
  print({"AccountNumS": 5475835454})
  print({"BalanceS": 90343.04})
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
     print({"Checking Account Number": 5475835230})
     print({"Balance": 1900.86})
     print({"Saving Account Number": 5475835231})
     print({"Balance": 500876.89})
    elif FirstName == 'Erica' and LastName == 'Johnson':
     print(FirstName)
     print(LastName)
     print({"Checking Account Number": 5475806426})
     print({"Balance": 3940.86})
     print({"Saving Account Number": 5475806427})
     print({"Balance": 4087.89})
    elif FirstName == 'Kim' and LastName == 'Thomas':
     print(FirstName)
     print(LastName)
     print({"Checking Account Number": 5475835453})
     print({"Balance": 6764.32})
     print({"Saving Account Number": 5475835454})
     print({"Balance": 90343.04})
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

