import cs50
from sys import argv
import csv

db = cs50.SQL("sqlite:///students.db")
List = db.execute("SELECT * FROM HogwartsStudents ORDER BY lastname") #db.execute returns python dict
check = False

if len(argv) != 2:
    print("Invalid command-line arguments")
    exit(1)

houseRequest = str(argv[1])

for row in List:
    firstname = row["firstname"]
    middlename = row["middlename"]
    lastname = row["lastname"]
    birth = row["birth"]
    house = row["house"]

    if house == houseRequest:
        if check == False:
            check = True
        if middlename == None:
            print(f"{firstname} {lastname}, born {birth}")
        else:
            print(f"{firstname} {middlename} {lastname}, born {birth}")

if check == False:
        print("Please check your house spelling")
