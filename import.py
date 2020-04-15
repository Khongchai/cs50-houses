from sys import argv
import csv
import cs50

if len(argv) != 2:# python is not part of command-line count
    print("Error: Invalid command line")
    exit(1)

open("students.db", "w").close() #open for write, delete old info everytime it runs
db = cs50.SQL("sqlite:///students.db") #sql query will now modify this database
db.execute("CREATE TABLE HogwartsStudents(firstname TEXT, middlename TEXT, lastname TEXT, house TEXT, birth NUMERIC)")

with open(argv[1], "r") as file:
    CharactersList = csv.DictReader(file)
    for row in CharactersList:

        splitName = row["name"].split()
        if len(splitName) == 3:
            db.execute("INSERT INTO HogwartsStudents(firstname, middlename, lastname, house, birth) VALUES(?, ?, ?, ?, ?)",
            splitName[0], splitName[1], splitName[2], row["house"], row["birth"])
        else:
            db.execute("INSERT INTO HogwartsStudents(firstname, middlename, lastname, house, birth) VALUES(?, NULL, ?, ?, ?)",
            splitName[0], splitName[1], row["house"], row["birth"])







