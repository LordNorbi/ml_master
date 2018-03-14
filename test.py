import os, sys, sqlite3
import time
import random
import numpy as np
#from tools import ml_machine as ml
from tools.ml_machine import ml_machine as ml
from tools.machine import machine as mach

db_name = "db/"+"ml_data"+".db" #name of the db created and used
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
    output(db_name+" contains "+str(getNumberOfEntries())+" entries and "+str(getMachines())+" learned Machines")

def createDB():
    #create new db
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("DB created!")
    createTable()
    createMLTable()
    createData()

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
    sql = "CREATE TABLE IF NOT EXISTS Machines(Id INT, Name STRING, Score FLOAT, Precision_0 FLOAT, Recall_0 FLOAT, F1_0 FLOAT, Support_0 FLOAT, Precision_1 FLOAT, Recall_1 FLOAT, F1_1 FLOAT, Support_1 FLOAT, Duration FLOAT, Time String, Object STRING)"
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
        insert(id,tup,attribute,"Data")
        id+=1

    end = time.time()
    output("Writing finished in: "+str(end-start))


def insert(id,tup,attr,table):
    if (len(attr)-1)!= len(tup):
        output("Missmatch at Insertion. EXIT")
        return()

    sql = "INSERT INTO "+table+"("
    for j in range(len(attr)):
        if j!=0:
            sql+=","+attr[j]
        else:
            sql+=attr[j]

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

def getMachines():
    sql = "SELECT count(Id) FROM Machines where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

def getData():
    sql = "SELECT * FROM Data"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)

    data = []
    currentline = db_cursor.fetchone()
    if currentline==None:
        return(0)
    while currentline != None:
        data.append(currentline)
        currentline = db_cursor.fetchone()
    data = np.array(data)
    return data[:, [1,2]],data[:, 3]

def getOverviewOfResults():
    #get data from db
    sql = "SELECT Name, Score FROM Machines where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)

    #extract data
    data = []
    currentline = db_cursor.fetchone()
    while currentline != None:
        data.append(currentline)
        currentline = db_cursor.fetchone()

    data = np.array(data)
    print data
    return()

def main():
    checkDB()
    if create_new_data:
        eraseData()
        createData()

    X_data, y_data = getData()


    m = ml(X_data, y_data, amount_of_data)

    #m.dec_tree = mach
    #m.dec_tree.fitted = m.loadMachine("2_DEC_tree_2018-03-14.pkl")
    #m.bench(m.dec_tree)

    #m.createSVM_poly()
    #m.bench(m.svm_pol)
    #m.saveMachine(db_connection,m.svm_pol)

    #m.createDEC_tree()
    #m.bench(m.dec_tree)
    #m.saveMachine(db_connection,m.dec_tree)

    #m.createK_nearest()
    #m.bench(m.k_nearest)
    #m.saveMachine(db_connection,m.k_nearest)

    #m.createLOGIST_reg()
    #m.bench(m.logist_reg)
    #m.saveMachine(db_connection,m.logist_reg)

    #m.createNAIVE_bay()
    #m.bench(m.naive_bay)
    #m.saveMachine(db_connection,m.naive_bay)

    getOverviewOfResults()


    closeDB()

if __name__ == "__main__":
    main()
