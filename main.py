import os, sqlite3
import time
import random
import numpy as np
import logging

from tools.ml_machine import ml_machine as ml
from tools.machine import Machine

#db_name = "db/big_set"+".db"
db_name = "db/all_sets"+".db"


table_name = "Dataset4"
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
    
    logger = logging.getLogger('OutputMonitorLogger')
    hdlr = logging.FileHandler('./log/ml.log')
    formatter = logging.Formatter('%(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    
    logger.info("-------------------------------------------")
    
    checkDB()
    X_data, y_data = getData()
    m = ml(X_data, y_data, logger)

    #m.dec_tree = Machine()
    #m.dec_tree.fitted = m.loadMachine("1_DEC_tree_2018-03-14.pkl")
    #m.bench(m.dec_tree)

    svmtune = True
    dectune = False
    knntune = False
    logtune = False
    navtune = False
    
    svm = False
    dec = False
    knn = False
    log = False
    nav = False



    #kernel=['poly','rbf']                                      #   -
    tol = [1, 0.1, 5, 0.001, 0.0001]
    tol = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    cs = [1, 1.5, 2, 5, 10]                                     #   5
    #ws = [{0:1,1:1},{0:1,1:3},{0:3,1:1},{0:10,1:1},{0:1,1:10}]  #   5
    xs = [5,7,9,12]                                                  #   2
    c= 'None'                                                                #  50
    if svmtune:
        for t in tol:
            #for c in cs:
                    logger.info("SVM: rbf, tol: "+str(t)+", C: "+str(c))
                    i = m.createSVM_poly(mkernel = 'rbf', mtol = t, mC = c)
                    m.bench(m.svm_pol_list[i])
                    m.saveMachine(db_connection,m.svm_pol_list[i])
    t = 'None'
    x= 'None'
    if svmtune:
        for t in tol:
            #for x in xs:
            #for c in cs:
                    logger.info("SVM: poly, tol: "+str(t)+", C: "+str(c))
                    i = m.createSVM_poly(mkernel = 'poly', mtol = t, mC = c, mdegree=x)
                    m.bench(m.svm_pol_list[i])
                    m.saveMachine(db_connection,m.svm_pol_list[i])


    solv=['sag','saga']                                         #   2
    pen = ['str','l1','l2']                                     #   3
    iter = [500,1000,10000]                                     #   3
    tol = [1, 0.1, 5, 0.001, 0.0001]                            #   5
                                                                #  60
    if logtune:
        for so in solv:
            for p in pen:
                for t in tol:
                    for it in iter:
                        if so =='sag':
                            if p =='l2':
                                logger.info("Log:  solv: "+so+",  penalty: "+p+",  tol:"+ str(t) + ",  iterations: "+str(it))
                                i = m.createLOGIST_reg(csolver=so, cpenalty=p, ctol=t, cmax_iter=it)
                                m.bench(m.logist_reg_list[i])
                                m.saveMachine(db_connection,m.logist_reg_list[i])
                        else:
                            logger.info("Log:  solv: "+so+",  penalty: "+p+",  tol:"+ str(t) + ",  iterations: "+str(it))
                            i = m.createLOGIST_reg(csolver=so, cpenalty=p, ctol=t, cmax_iter=it)
                            m.bench(m.logist_reg_list[i])
                            m.saveMachine(db_connection,m.logist_reg_list[i])
    
    
    splitter = ['best','random']                                #   2
    max_depth = [None,10,15,20]                                 #   4
    min_samples_split = [2,5,10]                                #   3
    min_samples_leaf = [1,2,5,10]                               #   4
                                                                #  96
    if dectune:
        for split in splitter:
            for md in max_depth:
                for mss in min_samples_split:
                    for msl in min_samples_leaf:
                        logger.info("Log:  splitter: "+split+",  max_depth: "+str(md)+",  min_sample_split:"+ str(mss) + ",  min_sample_leaf: "+str(msl))
                        i = m.createDEC_tree(csplitter = split, cmax_depth = md, cmin_samples_leaf = msl, cmin_samples_split = mss)
                        m.bench(m.dec_tree_list[i])
                        m.saveMachine(db_connection,m.dec_tree_list[i])


    ks = [1,2,5,10,25]                                          #   5
    weights = ['uniform', 'distance']                           #   2
    algorithm = ['ball_tree', 'kd_tree', 'brute']               #   3
                                                                #  30
    if knntune:
        for k in ks:
            for w in weights:
                for al in algorithm:
                    logger.info("KNN:  K: "+str(k)+",  algorithm: "+al+",  weight:"+ w)
                    i = m.createK_nearest(neighbors = k, cweights = w, calgorithm=al )
                    m.bench(m.k_nearest_list[i])
                    m.saveMachine(db_connection,m.k_nearest_list[i])


    verfahren = ['gaussian','multinomial','bernoulli']          #   3
    if navtune:
        for ver in verfahren:
            logger.info("NaB:  Verfahren: "+ver)
            i = m.createNAIVE_bay(type = ver)
            m.bench(m.naive_bay_list[i])
            m.saveMachine(db_connection,m.naive_bay_list[i])


    if svm:
        i = m.createSVM_poly()
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
        i = m.createNAIVE_bay()
        m.bench(m.naive_bay_list[i])
        m.saveMachine(db_connection,m.naive_bay_list[i])

    getOverviewOfResults()

    #getData()

    closeDB()

if __name__ == "__main__":
    main()
