# SimpleDB, created by Aspire
# The purpose of this project was to test out how good is the JSON system was in the Python.
# You can apply this to your Discord Bot or any of your Python program.

# Importing required modules
import os, sys, time
from colorama import *
from os import path
import random
import uuid

os.system("cls")

# Functions to create database
def generate_token(string_length=10):
    random = str(uuid.uuid4()) # Convert UUID format to a string.
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length] # Return the random string.

def create_database(username, token):
    if path.exists(f"../database/{username}.json"):
        print("[ERROR]: That username is already existed in the database.")
    else:
        db = '{ "username": "' + username + '", "token": "' + token + '" }'
        dbfile = open(f"../database/{username}.json", "w")
        dbfile.write(db) # This is where we call the "db" variable to create database formst.
        dbfile.close
        print(f"""
==================================
     -- Database Created --
==================================
Username : {username}
Token : {token}
==================================
        """)

def remove_database(username):
    if path.exists(f"../database/{username}.json"):
        os.remove(f"../database/{username}.json")
        print(f"[DELETE]: Database {username} has been deleted!")
    else:
        print("[ERROR]: That username is not even registered in the database.")

# Main functions
def main():
    print("""
=====================================
 SimpleDB - Created by : Aspire#0007
   -- Please take a choice here! --
   1.) Create database
   2.) Remove database
=====================================
    """)
    choice = input("Select [1/2]:")
    if choice == "1":
        userinput = input("Username : ")
        usertoken = generate_token(10)
        create_database(userinput, usertoken)
    if choice == "2":
        userinput = input("Username : ")
        remove_database(userinput)

# Start the main functions
if __name__ == "__main__":
    main()