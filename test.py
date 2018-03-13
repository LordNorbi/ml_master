import os, sys, sqlite3
import time
import random
from tools import ml_machine as ml

db_name = "ml_data"+".db" #name of the db created and used
amount_of_data = 30
attribute = ["Id","Period1","Period2","Deadline_Reached"]
types_of_attributes = ["INT","INT","INT","INT"] #Booleans are stores as INT (0 or 1)
create_new_data = False # True or False
db_connection = None

def output(msg):
    for line in msg.splitlines():
        print "Main: "+line

def checkDB():
    if not os.path.exists(db_name):
        print "Datenbank "+db_name+" nicht vorhanden - Datenbank wird anglegt."
        createDB()
        return()
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("Datenbank "+db_name+" found!")
    output(db_name+" contains "+str(getNumberOfEntries())+" entries")

def createDB():
    #create new db
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("DB created!")
    createTable()
    createMLTable()

def createTable():

    db_cursor = db_connection.cursor()

    #Check if Attributes and Types maches
    if len(attribute)!= len(types_of_attributes):
        output("Missmatch Attribute and Types! EXIT")
        return()

    #create the db Tables
    sql = "CREATE TABLE IF NOT EXISTS Data("
    for i in range(len(attribute)):
        if i!=0:
            sql+=","+attribute[i]+" "+types_of_attributes[i]
        else:
            sql+=attribute[i]+" "+types_of_attributes[i]

    sql+=")"
    db_cursor.execute(sql)
    db_connection.commit()

    output("Table "+db_name+" mit "+ sql +" angelegt")
    return()

def createMLTable():
    db_cursor = db_connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Machines(Id INT, Name STRING, Precision FLOAT, Recall FLOAT, F1 FLOAT, Support FLOAT, Duration FLOAT, Time TIMESTAMP)"
    db_cursor.execute(sql)
    db_connection.commit()
    output("Machine Table succesfully created")

def eraseData():
    output("Start DB erase.")
    start = time.time()
    db_cursor = db_connection.cursor()
    sql = "Drop Table Data"
    db_cursor.execute(sql)
    db_connection.commit()
    createTable()
    end = time.time()
    output("Erasion completed in: "+str(end-start))

def createData():

    tmp_tuple = []

    start = time.time()

    # change to 2 for more test data
    num_tests = 1

    #fill tuple data
    for i in range(int(amount_of_data*0.5*num_tests)):
        for j in range(int(amount_of_data*0.5*num_tests)):
            period1 = 200+i*20/num_tests + int(random.random()*10)
            period2 = 240+j*20/num_tests + int(random.random()*10)

            value = period1 * i * period1 + period2 * period2 * j  <  2500000.0 * num_tests + random.random() * 500000
            value_int = 0
            if value:
                value_int = 1
            tmp_tuple.append((period1, period2, value_int))
            #tmp_tuple.append((period1, period2, period1 + period2  <  750.0 * num_tests + random.random() * 10))

    end = time.time()
    output("Test data generated! Time needed: "+str(end-start))



    #Write tmp_data to db
    output("Write tmp data to database...")
    start = time.time()
    id = 0
    for tup in tmp_tuple:
        insert(id,tup)
        id+=1

    end = time.time()
    output("Writing finished in: "+str(end-start))


def insert(id,tup):
    sql = "INSERT INTO Data("
    for j in range(len(attribute)):
        if j!=0:
            sql+=","+attribute[j]
        else:
            sql+=attribute[j]

    sql+=")VALUES("


    for i in range(len(tup)):
        if i!=0:
            sql+=","+str(tup[i])
        else:
            sql+=str(id)+","+str(tup[i])
    sql+=")"
    #print sql
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    db_connection.commit()


def closeDB():
    db_connection.commit()
    db_connection.close()

def getNumberOfEntries():
    sql = "SELECT count(Id) FROM Data where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

def getData():
    sql = "SELECT * FROM Data where ID = 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    print db_cursor.fetchone
    print db_cursor.fetchone

def main():
    checkDB()
    if create_new_data:
        eraseData()
        createData()

    X_data = getData()
    y_data = []

    #m = ml.ml_machine(X_data, y_data)
    #m.createSVM_poly()

    closeDB()

if __name__ == "__main__":
    main()
