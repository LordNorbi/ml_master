import os, sqlite3
import time
import random
import numpy as np
import logging

from tools.ml_machine import ml_machine as ml
from tools.machine import Machine

db_name = "db/big_set"+".db"


attribute = ["Set_ID", "Priority01", "Deadline01", "Quota01", "PKG01", "Arg01", "Period01", "Number_of_Jobs01", "Offset01", "Priority02", "Deadline02", "Quota02", "PKG02", "Arg02", "Period02", "Number_of_Jobs02", "Offset02", "Priority03", "Deadline03", "Quota03", "PKG03", "Arg03", "Period03", "Number_of_Jobs03", "Offset03", "Priority04", "Deadline04", "Quota04", "PKG04", "Arg04", "Period05", "Number_of_Jobs05", "Offset05", "Priority05", "Deadline05", "Quota05", "PKG05", "Arg05", "Period05", "Number_of_Jobs05", "Offset05", "Exit_Value"]

types_of_attributes = [ "INT", "INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT", "INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT", "INT" ]



table_name = "Dataset"
create_new_data = False # True or False
db_connection = None

def output(msg):
    for line in msg.splitlines():
        print("Main: "+line)

def checkDB():
    if not os.path.exists(db_name):
        print("Datenbank "+db_name+" nicht vorhanden - Datenbank wird anglegt.")
        return()
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("Datenbank "+db_name+" found!")
    output("db_name:" + db_name+" table_name: "+ table_name)
    output(db_name+" contains "+str(getNumberOfEntries())+" entries and "+str(getMachines())+" learned Machines")


def createMLTable():
    db_cursor = db_connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Machines(Id INT, Name STRING, Score FLOAT, Precision_0 FLOAT, Recall_0 FLOAT, F1_0 FLOAT, Support_0 FLOAT, Precision_1 FLOAT, Recall_1 FLOAT, F1_1 FLOAT, Support_1 FLOAT, Duration FLOAT, Time String, Object STRING)"
    db_cursor.execute(sql)
    db_connection.commit()
    output("Machine Table succesfully created")


def closeDB():
    db_connection.commit()
    db_connection.close()

def getNumberOfEntries():
    sql = "SELECT count(Set_ID) FROM "+table_name+" where Set_ID >= 0" # fix id to the name of the id in yout table
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

def getMachines():
    sql = "SELECT count(Id) FROM Machines where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

def getData():
    sql = "SELECT * FROM "+table_name
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)

    data = []
    currentline = db_cursor.fetchone()
    if currentline==None:
        return(0)
    
    #store data from db in arry
    while currentline != None:
        data.append(currentline)
        currentline = db_cursor.fetchone()
    data = np.array(data)

    #check if there is data
    if len(data)== 0:
        output("There is no Data")
        return()

    #seperate Results from data
    i = 0
    range = []
    while i < (len(data[0])-1):         # last field for result
        if i != 0:                      # 0 is the id field
            range.append(i)
        i+=1
    
    return data[:,range],data[:, (len(data[0])-1)]

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
    print(data)
    return()

def main():
    checkDB()
    X_data, y_data = getData()
    m = ml(X_data, y_data)

    #m.dec_tree = Machine()
    #m.dec_tree.fitted = m.loadMachine("1_DEC_tree_2018-03-14.pkl")
    #m.bench(m.dec_tree)

    svmtune = True
    svm = False
    dec = False
    knn = False
    log = False
    nav = False

    logger = logging.getLogger('OutputMonitorLogger')
    hdlr = logging.FileHandler('./log/ml.log')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    kernel=['poly','rbf']
    tol = [1,0.1,0.0025,0.002,0.0015,0.001,0.00075,0.0005,0.00025,0.000001]
    cs = [5,4,3,2,1.5,1,0.75,0.5,0.25,0.1]
    ws = [{0:1,1:1},{0:1,1:2},{0:1,1:3},{0:1,1:4},{0:2,1:1},{0:3,1:1},{0:4,1:1},{0:1,1:10},{0:10,1:1}]
    xs = [5,6,7,8,9,10]


    if svmtune:
        for t in tol:
            #for x in xs:
                for c in cs:
                    for w in ws:
                        logger.info("SVM: rbf, tol: "+str(t)+"C: "+str(c)+" weight: "+str(w))
                        m.createSVM_poly(mkernel = 'rbf', mtol = t, mC = c, mclass_weight = w )
                        m.bench(m.svm_pol)
                        logger.info(m.saveMachine(db_connection,m.svm_pol))



    if svm:
        m.createSVM_poly(mdegree=5, mkernel='rbf', mclass_weight={0: 1,1:3})
        #m.createSVM_poly()
        m.bench(m.svm_pol)
        m.saveMachine(db_connection,m.svm_pol)
    if dec:
        m.createDEC_tree()
        m.bench(m.dec_tree)
        m.saveMachine(db_connection,m.dec_tree)
    if knn:
        m.createK_nearest()
        m.bench(m.k_nearest)
        m.saveMachine(db_connection,m.k_nearest)
    if log:
        m.createLOGIST_reg()
        m.bench(m.logist_reg)
        m.saveMachine(db_connection,m.logist_reg)

    if nav:
        m.createNAIVE_bay()
        m.bench(m.naive_bay)
        m.saveMachine(db_connection,m.naive_bay)

    getOverviewOfResults()

    #getData()

    closeDB()

if __name__ == "__main__":
    main()
