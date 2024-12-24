#importing the sqlite database for storage

import sqlite3

#Establishing a connection with the sqlite database

con = sqlite3.connect("AddressBook.db")

#Creating a cursor

sqlcur = con.cursor()
