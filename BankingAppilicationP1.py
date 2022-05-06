from ast import And, For
import collections
from re import I, X
from telnetlib import STATUS
from tkinter import FIRST
from unittest import result
from matplotlib.pyplot import close
import pymongo
from pymongo import MongoClient
import json


myclient = MongoClient() 
db = myclient.Project1
collections = db.account

class BankingAppilication :

 FirstName = ""
 LastName = ""
 AccountNumC = ""
 AccountNumS = ""
 BalanceC = ""
 NewBalanceCw = ""
 NewBalanceC = ""

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

# Import Data
def ImportData() :
  with open('account.json') as a1:
   file_data = json.load(a1)
  collections.insert_many(file_data)

def DisplayAll():
    FirstName = input("Enter First Name: ")
    LastName = input("Enter Last Name: ")
    print(collections.find_one( {"FirstName" : (FirstName) }))

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

   print("\t2. Deposit")

   print("\t3. Withdraw")

   print("\t4. Display Account Information")

   print("\t5. Import Data")

   print("\t6. Exit")

   print("\tSelect Your Option (1-6): ")

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

     ImportData()

   elif BC == '6':

       print("\tThanks for using Apple Banking System")

       break

   else :

       print("Invalid selection")  

       BC = input("Enter your choice : ")

