import os, sqlite3
import time
import random
import numpy as np
#from tools import ml_machine as ml
from tools.ml_machine import ml_machine as ml
from tools.machine import Machine

#db_name = "db/"+"ml_data"+".db" #name of the db created and used
#db_name = "db/"+"training_data_4"+".db"
db_name = "db/big_set"+".db"

#attribute = ["id", "Task1_id", "Task1_executiontime","Task1_criticaltime","Task1_size","Task1_priority"," Task1_period","Task1_offset","Task1_RAMquota","Task1_arg1","Task2_id","Task2_executiontime","Task2_criticaltime","Task2_size","Task2_priority","Task2_period","Task2_offset","Task2_RAMquota","Task2_arg1","Task3_id","Task3_executiontime","Task3_criticaltime","Task3_size","Task3_priority","Task3_period","Task3_offset","Task3_RAMquota","Task3_arg1","Task4_id","Task4_executiontime","Task4_criticaltime","Task4_size","Task4_priority","Task4_period","Task4_offset","Task4_RAMquota","Task4_arg1","Task5_id","Task5_executiontime","Task5_criticaltime","Task5_size","Task5_priority","Task5_period","Task5_offset","Task5_RAMquota","Task5_arg1","Task6_id","Task6_executiontime","Task6_criticaltime","Task6_size","Task6_priority","Task6_period","Task6_offset","Task6_RAMquota","Task6_arg1","Task7_id","Task7_executiontime","Task7_criticaltime","Task7_size","Task7_priority","Task7_period","Task7_offset","Task7_RAMquota","Task7_arg1","succ"] #["Id","Period1","Period2","Deadline_Reached"]
#attribute = ["id", "Task1_id", "Task1_criticaltime", "Task1_arg1", "Task2_id", "Task2_criticaltime", "Task2_arg1", "Task3_id", "Task3_criticaltime", "Task3_arg1", "Task4_id", "Task4_criticaltime", "Task4_arg1", "Task5_id", "Task5_criticaltime", "Task5_arg1", "Task6_id", "Task6_criticaltime", "Task6_arg1", "Task7_id", "Task7_criticaltime", "Task7_arg1", "Fail"]
attribute = ["Set_ID", "Priority01", "Deadline01", "Quota01", "PKG01", "Arg01", "Period01", "Number_of_Jobs01", "Offset01", "Priority02", "Deadline02", "Quota02", "PKG02", "Arg02", "Period02", "Number_of_Jobs02", "Offset02", "Priority03", "Deadline03", "Quota03", "PKG03", "Arg03", "Period03", "Number_of_Jobs03", "Offset03", "Priority04", "Deadline04", "Quota04", "PKG04", "Arg04", "Period05", "Number_of_Jobs05", "Offset05", "Priority05", "Deadline05", "Quota05", "PKG05", "Arg05", "Period05", "Number_of_Jobs05", "Offset05", "Exit_Value"]
#types_of_attributes = ["TEXT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT"] #["INT","INT","INT","INT"] #Booleans are stores as INT (0 or 1)
#types_of_attributes = ["TEXT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT","INT"]
types_of_attributes = [ "INT", "INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT", "INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT","INT", "INT", "STRING", "STRING", "INT", "INT", "INT", "INT", "INT" ]


#table_name = "training" #"Data"
table_name = "Dataset"
create_new_data = False # True or False
db_connection = None

def output(msg):
    for line in msg.splitlines():
        print("Main: "+line)

def checkDB():
    if not os.path.exists(db_name):
        print("Datenbank "+db_name+" nicht vorhanden - Datenbank wird anglegt.")
        #createDB()
        return()
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("Datenbank "+db_name+" found!")
    output("db_name:" + db_name+" table_name: "+ table_name)
    output(db_name+" contains "+str(getNumberOfEntries())+" entries and "+str(getMachines())+" learned Machines")

def createDB():
    #create new db
    global db_connection
    db_connection = sqlite3.connect(db_name)
    output("DB created!")
    createTable()
    createMLTable()
    #createData()

def createTable():

    db_cursor = db_connection.cursor()

    #Check if Attributes and Types maches
    if len(attribute)!= len(types_of_attributes):
        output("Missmatch Attribute and Types! EXIT")
        return()

    #create the db Tables
    sql = "CREATE TABLE IF NOT EXISTS "+table_name+" ("
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
        insert(id,tup,attribute,table_name)
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
    
    if create_new_data:
        eraseData()
        createData()

    X_data, y_data = getData()

    print(str(len(X_data)))
    #X_data = X_data[:1000]
    #print(str(len(X_data)))
    #y_data = y_data[:1000]
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
                        print("Polynom "+str(5)+" tol: "+str(t))
                        m.createSVM_poly(mkernel = 'rbf', mtol = t, mC = c, mclass_weight = w )
                        m.bench(m.svm_pol)
                        m.saveMachine(db_connection,m.svm_pol)



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
