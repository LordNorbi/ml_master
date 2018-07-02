import time
import datetime
import _pickle as cPickle
from sklearn import svm
from sklearn import metrics
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from .machine import Machine


class ml_machine:

    X_train = []
    y_train = []
    X_test = []
    y_test = []

    svm_pol = None
    dec_tree = None
    k_nearest = None
    logist_reg = None
    naive_bay = None

    def __init__(self, X_data, y_data, split=0.66):
        neu = []
        y_data = [0 if element == '-1' else element for element in y_data]
        y_data = [1 if element == '1' else element for element in y_data]
        #print(y_data)
        for line in X_data:
            #print(line)
            line = [10 if element == '10M' else element for element in line]
            line = [1 if element == 'hey' else element for element in line]
            line = [2 if element == 'pi' else element for element in line]
            line = [3 if element == 'cond_42' else element for element in line]
            line = [4 if element == 'cond_mod' else element for element in line]
            line = [5 if element == 'tumatmul' else element for element in line]
            line = list(map(int, line))
            neu.append(line)
            #print(line)
        
        X_data = neu
        #X_data = X_data.astype(int)
        
        #print(X_data)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_data, y_data, test_size=split, random_state=0)
        print("size of Train: "+str(len(self.X_train)))
        print("size of Test: "+str(len(self.X_test)))

        #i = 0
        #x = 0
        #
        #while i < len(self.y_train):
        #    x = x + self.y_train[i]
        #    i = i+1;
        #print("finished "+str(x))
        #i = 0
        #x = 0
        #while i < len(self.y_test):
        #    x = x + self.y_train[i]
        #    i = i+1;
        #print("finished "+str(x))

        #print(self.X_train)
        #print(self.y_train)
        #x = 0
        #while x < 30:
            #print(self.X_train[x])
            #x = x+1

    def output(self, msg):
        for line in msg.splitlines():
            print("ML: "+line)

    #@profile #for memory usage with python -m memory_profiler main.py
    def createSVM_poly(self, mkernel='poly',mdegree=2,mcache_size=7000, mtol=0.0001, mclass_weight={0: 1,1:3}, mC=1):
        self.svm_pol = Machine()
        self.svm_pol.name = "SVM_pol"
        self.output("SVM poly created training will start soon...")
        start = time.time()
        self.svm_pol.unfitted = svm.SVC(kernel=mkernel, degree=mdegree,cache_size=mcache_size, tol=mtol, class_weight=mclass_weight, C=mC)
        self.output("unfitted")
        self.svm_pol.fitted = self.svm_pol.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.svm_pol.duration = end - start
        self.output("SVM poly done in: " +  str(self.svm_pol.duration) + " s")
        return()

    def createDEC_tree(self, max_depth = 3, min_samples_leaf = 5):
        self.dec_tree = Machine()
        self.dec_tree.name="DEC_tree"
        self.output("DEC created training will start soon...")
        start = time.time()
        self.dec_tree.unfitted = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth, min_samples_leaf= min_samples_leaf )
        self.dec_tree.fitted = self.dec_tree.unfitted.fit(self.X_train,self.y_train)
        end = time.time()
        self.dec_tree.duration = end - start
        self.output("Dec Tree done in: " +  str(self.dec_tree.duration) + " s")

        return()

    def createK_nearest(self,neighbors = 3):
        self.k_nearest = Machine()
        self.k_nearest.name = "k_nearest"
        self.output("KNN poly created training will start soon...")
        start = time.time()
        self.k_nearest.unfitted = KNeighborsClassifier(n_neighbors=neighbors)
        self.k_nearest.fitted = self.k_nearest.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.k_nearest.duration = end - start
        self.output("k-nearest done in: " +  str(self.k_nearest.duration) + " s")

        return()

    def createLOGIST_reg(self, c=1e5):
        self.logist_reg = Machine()
        self.logist_reg.name = "logist_reg"
        self.output("Logistic_reg poly created training will start soon...")
        start = time.time()
        self.logist_reg.unfitted = linear_model.LogisticRegression(C=c)
        self.logist_reg.fitted = self.k_nearest.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.logist_reg.duration = end - start
        self.output("logistc_reg done in: " +  str(self.logist_reg.duration) + " s")

        return()

    def createNAIVE_bay(self):
        self.naive_bay = Machine()
        self.naive_bay.name = "naive_bay"
        self.output("naive:bay poly created training will start soon...")
        start = time.time()
        self.naive_bay.unfitted = GaussianNB()
        self.naive_bay.fitted = self.naive_bay.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.naive_bay.duration = end - start
        self.output("naive_bay done in: " +  str(self.naive_bay.duration) + " s")

        return()

    #@profile
    def bench(self,machine):
        if machine == None:
            self.output("There is no SVM to benchmark!")
            return()

        machine.score = machine.fitted.score(self.X_test,self.y_test)
        print("Score: ", machine.score)

        y_pred = machine.fitted.predict(self.X_test)
        report = metrics.classification_report(self.y_test, y_pred)

        list=report.encode('ascii','ignore').split()
        
        self.output(str(len(list)))

        if len(list) ==16:
            if list[5] == '/':
                list[5]='0'
                self.output("canged")
            if list[6] == '/':
                list[6]='0'
                self.output("canged")
            if list[7] == '/':
                list[7]='0'
                self.output("canged")
            if list[8] == '/':
                list[8]='0'
                self.output("canged")
            if list[12] == '/':
                list[12]='0'
                self.output("canged")
            if list[13] == '/':
                list[13]='0'
                self.output("canged")
            if list[14] == '/':
                list[14]='0'
                self.output("canged")
            if list[15] == '/':
                list[15]='0'
                self.output("canged")
            machine.precision = float(list[5]), float(list[12]) #Precision for class 0 and avg/total
            machine.recall = float(list[6]), float(list[13])
            machine.f1 = float(list[7]), float(list[14])
            machine.support = float(list[8]), float(list[15])

        if len(list) ==21:
            if list[5] == '/':
                list[5]='0'
                self.output("canged")
            if list[6] == '/':
                list[6]='0'
                self.output("canged")
            if list[7] == '/':
                list[7]='0'
                self.output("canged")
            if list[8] == '/':
                list[8]='0'
                self.output("canged")
            if list[10] == '/':
                list[10]='0'
                self.output("canged")
            if list[11] == '/':
                list[11]='0'
                self.output("canged")
            if list[12] == '/':
                list[12]='0'
                self.output("canged")
            if list[13] == '/':
                list[13]='0'
                self.output("canged")
            if list[17] == '/':
                list[17]='0'
                self.output("canged")
            if list[18] == '/':
                list[18]='0'
                self.output("canged")
            if list[19] == '/':
                list[19]='0'
                self.output("canged")
            if list[20] == '/':
                list[20]='0'
                self.output("canged")
            machine.precision = float(list[5]), float(list[10]), float(list[17]) #Precision for class 0,1 and avg/total
            machine.recall = float(list[6]), float(list[11]), float(list[18])
            machine.f1 = float(list[7]), float(list[12]), float(list[19])
            machine.support = float(list[8]), float(list[13]), float(list[20])


        return()

    def saveMachine(self,db_connection,machine):

        #check if any value is none
        if machine.name==None or machine.precision==None or machine.recall==None or machine.f1==None or machine.support==None or machine.duration==None:
            #bench the svm to get the required data
            self.bench(machine)

        db_cursor = db_connection.cursor()

        #get max id to calculate the next id
        sql = "Select max(Id) from Machines"
        db_cursor.execute(sql)
        id= db_cursor.fetchone()[0]
        if id == None:
            id = 0
        else:
            id += 1

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #SQL format: YYYY-MM-DD HH:MI:SS
        #print timestamp
        filename = str(id)+"_"+machine.name+"_"+timestamp[:10]+".pkl"

        #create sql statement
        sql = "Insert into Machines (Id, Name, Score, Precision_0, Recall_0, F1_0, Support_0, Precision_1, Recall_1, F1_1, Support_1, Duration, Time, Object) VALUES ("
        sql += str(id)+",'"+machine.name+"',"+str(machine.score)+","\
               +str(machine.precision[0])+","+ str(machine.recall[0])+","+str(machine.f1[0])+","+str(machine.support[0])+","\
               +str(machine.precision[1])+","+ str(machine.recall[1])+","+str(machine.f1[1])+","+str(machine.support[1])+","\
               +str(machine.duration)+",'"+str(timestamp)+"','"+str(filename)+"')"

        #write machine to file
        with open("saves/"+filename, 'wb') as fid:
            cPickle.dump(machine.fitted, fid)

        #print sql
        db_cursor.execute(sql)
        db_connection.commit()
        self.output("Save completed!")

    def loadMachine(self,filename):
        #read machine from file
        with open('saves/'+filename, 'rb') as fid:
            loaded_machine = cPickle.load(fid)

        self.output(filename+" loaded completed!")
        return loaded_machine
