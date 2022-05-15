from ast import And, For
import collections
from random import randint
from re import I, X
from telnetlib import STATUS
from tkinter import FIRST
from unittest import result
from matplotlib.pyplot import close
import pymongo
from pymongo import MongoClient
import json
import random
import string 

myclient = MongoClient() 
db = myclient.Project1
collections = db.account

class BankingAppilication :

 FirstName = ""
 LastName = ""
 AccountNumC = ""
 BalanceC = ""
 newBalance = ""

# Add New Customer
def Create() :
  FirstName = (input("Enter First Name: "))
  LastName = (input ("Enter Last Name: "))
  AccountNumC = random.randint(5475100000, 5475999999)  
  BalanceC = (input ("Enter deposit ammount: "))
  collections.insert_one({"FirstName" : FirstName, "LastName" : LastName, "AccountNumC" : AccountNumC, "BalanceC" : BalanceC})
  print("New customer account added successfully!")
  print(collections.find_one({"AccountNumC": AccountNumC}))

#Delete Customer
def Delete() :
 FirstName = (input("Enter First Name: "))
 LastName = (input ("Enter Last Name "))
 collections.delete_one({"FirstName" : FirstName})
 print("Customer account removed successfully!")

#Customer can deposit funds into account
def Deposit():
    AccountNumC =(input("Enter Checking Account Number: ")) 
    string = collections.find_one({"AccountNumC": (AccountNumC)})
    currentBalance = string["BalanceC"]
    amount = (input("Enter amount to be deposit: "))
    newBalance = int(currentBalance) + int(amount)
    collections.update_one( {"AccountNumC": AccountNumC }, { "$set" : {"newBalance" : newBalance} } ) 
    print(collections.find_one({"AccountNumC": AccountNumC}))

#Customer can withdraw funds out their account
def Withdraw():
    AccountNumC =(input("Enter Checking Account Number: ")) 
    string = collections.find_one({"AccountNumC": (AccountNumC)})
    currentBalance = string["BalanceC"]
    amount = (input("Enter amount to be deposit: "))
    newBalance = int(currentBalance) - int(amount)
    collections.update_one( {"AccountNumC": AccountNumC }, { "$set" : {"newBalance" : newBalance} } ) 
    print(collections.find_one({"AccountNumC": AccountNumC}))

#Viewing checking account
def Checking():
 AccountNumC=(input("Enter Checking Account Number: ")) 
 print(collections.find_one( {"AccountNumC" : (AccountNumC) }))

#View customer account information
def DisplayAll():
    FirstName = input("Enter First Name: ")
    LastName = input("Enter Last Name: ")
    print(collections.find_one( {"FirstName" : (FirstName)}))
  
#Introduction of the Banking Application
def Intro():

   print("\t\t\t\t*****************************")

   print("\t\t\t\t***REVATURE ONLINE BANKING***")
   
   print("\t\t\t\t*****************************")

   print("\t\t\t\t*We care about our customers*")

   print("\t\t\t\t*****************************")

# start of the program
BC = " "

num = 0

Intro()

while BC != 7:

   print("\tMain Menu")

   print("\t1. Checking Account")
   print("\t2. Deposit")
   print("\t3. Withdraw")
   print("\t4. Display Account Information")
   print("\t5. Create Customer Account")
   print("\t6. Remove Customer Account")
   print("\t7. Exit")
   print("\tSelect Your Option (1-7): ")

   BC = input()

   if BC == '1':

    Checking()
     
   elif BC == '2':

     Deposit()

   elif BC == '3':

     Withdraw()

   elif BC == '4':

     DisplayAll()

   elif BC == '5':
    
    Create()

   elif BC == '6':
    
    Delete()

   elif BC == '7':

       print("\tThanks for using Revature Banking System")

       break

   else :

       print("Invalid selection")  

       BC = input("Enter your choice : ")

