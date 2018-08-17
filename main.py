import os, sqlite3
import time
import random
import numpy as np
import logging

from tools.ml_machine import ml_machine as ml
from tools.machine import Machine
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC


#define the name of the database
db_name = "db/all-set_final-datasets"+".db"

#define the Datatset (name of the table in the database)
table_name = "Dataset5"

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

#creates the "Machine" Table. The Score of trainied Machines are stored in the Machine Table.
def createMLTable():
    db_cursor = db_connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Machines(Id INT, Name STRING, Score FLOAT, Precision_0 FLOAT, Recall_0 FLOAT, F1_0 FLOAT, Support_0 FLOAT, Precision_1 FLOAT, Recall_1 FLOAT, F1_1 FLOAT, Support_1 FLOAT, Duration FLOAT, Time String, Object STRING)"
    db_cursor.execute(sql)
    db_connection.commit()
    output("Machine Table succesfully created")


def closeDB():
    db_connection.commit()
    db_connection.close()

#returns the number of entries in the selectes dataset of the db.
def getNumberOfEntries():
    sql = "SELECT count(Set_ID) FROM "+table_name+" where Set_ID >= 0" # fix id to the name of the id in yout table
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

#returnes the count of the saved machines in the db.
def getMachines():
    sql = "SELECT count(Id) FROM Machines where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    return db_cursor.fetchone()[0]

#returns the selected dataset.
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

#prints the saved machines scores
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

#returns the saves machine scores
def getResults():
    #get data from db
    sql = "SELECT Score FROM Machines where Id >= 0"
    db_cursor = db_connection.cursor()
    db_cursor.execute(sql)
    
    #extract data
    data = []
    currentline = db_cursor.fetchone()
    while currentline != None:
        #print(currentline)
        data.append(currentline[0])
        currentline = db_cursor.fetchone()
    
    data = np.array(data)
    print(data)
    return()



def main():
    
    logger = logging.getLogger('OutputMonitorLogger')
    hdlr = logging.FileHandler('./log/ml.log')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    
    logger.info("-------------------------------------------")
    
    checkDB()
    #gets data
    X_data, y_data = getData()
    #creates helper-class
    m = ml(X_data, y_data, logger)


    #choose what you wanna do. Code see below
    svmtune = False
    dectune = False
    knntune = False
    logtune = False
    navtune = False
    
    svm = False
    dec = False
    knn = False
    log = False
    nav = False



    kernel=['poly','rbf']
    degree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    tol = [0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.50, 5, 10]
    cs = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 5, 10]
    # creates 15*15*11 + 15*11 Machiens (training&testing)
    if svmtune:
        for ker in kernel:
            if ker = 'poly':
                for deg in degree:
                    for t in tol:
                        for c in cs:
                            logger.info("SVM: "+ker+" degree: "+str(deg)+ " tol: "+str(t) + "c: "+str(c))
                            i = m.createSVM_poly(mkernel = ker, mdegree=deg, mC=c, mtol=t)
                            m.bench(m.svm_pol_list[i])
                            m.saveMachine(db_connection,m.svm_pol_list[i])
            #rbf kernel dont use degree
            else:
                    for t in tol:
                        for c in cs:
                            logger.info("SVM: "+ker+" degree: "+str(deg)+ " tol: "+str(t) + "c: "+str(c))
                            i = m.createSVM_poly(mkernel = ker, mdegree=deg, mC=c, mtol=t)
                            m.bench(m.svm_pol_list[i])
                            m.saveMachine(db_connection,m.svm_pol_list[i])



    solv=['sag','saga','liblinear']#be carefull some solver just support l2 penalty!
    pen = ['str','l1','l2']
    tol = [0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.50, 5, 10]
    cs = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 5, 10]
    # creates 3*3*15*11 Machiens (training&testing)
    if logtune:
        for so in solv:
            for p in pen:
                for t in tol:
                    for c in cs:
                        logger.info("Log:  solv: "+so+",  penalty: "+p+",  tol:"+ str(t) + ",  c: "+str(c))
                        i = m.createLOGIST_reg(csolver=so,cpenalty=p, ctol = t, cc = c)
                        m.bench(m.logist_reg_list[i])
                        m.saveMachine(db_connection,m.logist_reg_list[i])
    
    
    splitter = ['best','random']
    max_depth = [None,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,40,45,50]
    min_samples_split = [5,10,20,30,40,50,100,150,200,250,300,350,400,450]
    #creates 2*35*14 Machiens (training&testing)
    if dectune:
        for split in splitter:
            for md in max_depth:
                for mss in min_samples_split:
                        logger.info("DEC:  splitter: "+split+",  max_depth: "+str(md)+",  min_sample_split:"+ str(mss))
                        i = m.createDEC_tree(cmin_samples_split = mss, cmax_depth = md, csplitter = split)
                        m.bench(m.dec_tree_list[i])
                        m.saveMachine(db_connection,m.dec_tree_list[i])


    ks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,40,45,50]
    weights = ['uniform', 'distance']
    algorithm = ['auto','ball_tree', 'kd_tree', 'brute']
    # generates 34*2*4 Machines. (train&test)
    if knntune:
        for al in algorithm:
            for k in ks:
                for w in weights:
                    logger.info("KNN:   algorithm: "+al+",    K: "+str(k)+",    weight:"+ w)
                    i = m.createK_nearest(neighbors = k, cweights = w, calgorithm=al )
                    m.bench(m.k_nearest_list[i])
                    m.saveMachine(db_connection,m.k_nearest_list[i])


    verfahren = ['gaussian','multinomial','bernoulli']
    if navtune:
        for ver in verfahren:
            logger.info("NaB:  Verfahren: "+ver)
            i = m.createNAIVE_bay(type = ver)
            m.bench(m.naive_bay_list[i])
            m.saveMachine(db_connection,m.naive_bay_list[i])


    if svm:
        i = m.createSVM_poly(mkernel = 'poly')
        m.bench(m.svm_pol_list[i])
        m.saveMachine(db_connection,m.svm_pol_list[i])
        i = m.createSVM_poly(mkernel = 'rbf')
        m.bench(m.svm_pol_list[i])
        m.saveMachine(db_connection,m.svm_pol_list[i])
    if dec:
        i = m.createDEC_tree()
        m.bench(m.dec_tree_list[i])
        m.saveMachine(db_connection,m.dec_tree_list[i])
    if knn:
        i = m.createK_nearest()
        m.bench(m.k_nearest_list[i])
        m.saveMachine(db_connection,m.k_nearest_list[i])
    if log:
        i = m.createLOGIST_reg()
        m.bench(m.logist_reg_list[i])
        m.saveMachine(db_connection,m.logist_reg_list[i])

    if nav:
        i = m.createNAIVE_bay(type = 'gaussian')
        m.bench(m.naive_bay_list[i])
        m.saveMachine(db_connection,m.naive_bay_list[i])
        i = m.createNAIVE_bay(type = 'multinomial')
        m.bench(m.naive_bay_list[i])
        m.saveMachine(db_connection,m.naive_bay_list[i])
        i = m.createNAIVE_bay(type = 'bernoulli')
        m.bench(m.naive_bay_list[i])
        m.saveMachine(db_connection,m.naive_bay_list[i])


    getResults()

    closeDB()

if __name__ == "__main__":
    main()
