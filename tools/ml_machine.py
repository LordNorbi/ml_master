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
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

from .machine import Machine


class ml_machine:

    X_train = []
    y_train = []
    X_test = []
    y_test = []

    svm_pol_list = []
    dec_tree_list = []
    k_nearest_list = []
    logist_reg_list = []
    naive_bay_list = []
    logger = None

    def __init__(self, X_data, y_data, clogger, split=0.20):
        self.logger = clogger
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
        if self.logger!=None:
            self.logger.info(msg)
        #for line in msg.splitlines():
        #print("ML: "+line)

    #@profile #for memory usage with python -m memory_profiler main.py
    def createSVM_poly(self, mkernel='rbf',mdegree=5,mcache_size=1024, mtol=0.001, mclass_weight=None, mC=1):
        newmachine = Machine()
        newmachine.name = "SVM_"+mkernel
        
        #self.output("SVM poly created training will start soon...")
        newmachine.unfitted = svm.SVC(kernel=mkernel, degree=mdegree,cache_size=mcache_size, tol=mtol, class_weight=mclass_weight, C=mC)
        #self.output("unfitted")
        
        start = time.time()
        newmachine.fitted = newmachine.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        
        newmachine.duration = end - start
        #self.output("SVM poly done in: " +  str(newmachine.duration) + " s")
        
        self.svm_pol_list.append(newmachine)
        return(len(self.svm_pol_list)-1)

    def createDEC_tree(self, csplitter = 'best', cmax_depth = 3, cmin_samples_leaf = 1, cmin_samples_split = 2):
        newmachine = Machine()
        newmachine.name="DEC_tree"

        #self.output("DEC created training will start soon...")
        
        newmachine.unfitted = tree.DecisionTreeClassifier(criterion='entropy', splitter = csplitter, max_depth = cmax_depth, min_samples_leaf = cmin_samples_leaf, min_samples_split = cmin_samples_split )

        start = time.time()
        newmachine.fitted = newmachine.unfitted.fit(self.X_train,self.y_train)
        end = time.time()
        
        newmachine.duration = end - start
        #self.output("Dec Tree done in: " +  str(newmachine.duration) + " s")

        self.dec_tree_list.append(newmachine)
        return(len(self.dec_tree_list)-1)

    def createK_nearest(self, neighbors = 5, cweights = 'uniform', calgorithm='auto' ):
        newmachine = Machine()
        newmachine.name = "k_nearest"
        #self.output("KNN poly created training will start soon...")
        
        newmachine.unfitted = KNeighborsClassifier(n_neighbors=neighbors, weights = cweights, algorithm=calgorithm )

        start = time.time()
        newmachine.fitted = newmachine.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        
        newmachine.duration = end - start
        #self.output("k-nearest done in: " +  str(newmachine.duration) + " s")

        self.k_nearest_list.append(newmachine)
        return(len(self.k_nearest_list)-1)

    def createLOGIST_reg(self, csolver='liblinear', cpenalty='l2', ctol=0.0001, cmax_iter=100):
        newmachine = Machine()
        newmachine.name = "logist_reg"
        #self.output("Logistic_reg poly created training will start soon...")
        
        newmachine.unfitted = linear_model.LogisticRegression(solver=csolver,penalty=cpenalty,tol=ctol, max_iter=cmax_iter)

        start = time.time()
        newmachine.fitted = newmachine.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        
        newmachine.duration = end - start
        #self.output("logistc_reg done in: " +  str(newmachine.duration) + " s")

        self.logist_reg_list.append(newmachine)
        return(len(self.logist_reg_list)-1)

    def createNAIVE_bay(self,type = 'gaussian'):
        newmachine = Machine()
        newmachine.name = "naive_bay_"+type
        #self.output("naive:bay poly created training will start soon...")
        if type == 'gaussian':
            newmachine.unfitted = GaussianNB()
        if type == 'multinomial':
            newmachine.unfitted = MultinomialNB()
        if type == 'bernoulli':
            newmachine.unfitted = BernoulliNB()
        if newmachine.unfitted == None:
            print("NB type not available! NB was not created!")
            return()

        start = time.time()
        newmachine.fitted = newmachine.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        
        newmachine.duration = end - start
        #self.output("naive_bay done in: " +  str(newmachine.duration) + " s")
        self.naive_bay_list.append(newmachine)
        return(len(self.naive_bay_list)-1)

    #@profile
    def bench(self,machine):
        if machine == None:
            self.output("There is no SVM to benchmark!")
            return()

        machine.score = machine.fitted.score(self.X_test,self.y_test)
        self.output("Score: "+str(machine.score))

        y_pred = machine.fitted.predict(self.X_test)
        report = metrics.classification_report(self.y_test, y_pred)

        list=report.encode('ascii','ignore').split()
        
        #self.output(str(len(list)))

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
        self.output("Precision: "+str(machine.precision)+ " Recall: "+str(machine.recall)+" F1: "+str(machine.f1)+" Support: "+str(machine.support))

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
        self.output("Save completed! "+ filename)
        return()

    def loadMachine(self,filename):
        #read machine from file
        with open('saves/'+filename, 'rb') as fid:
            loaded_machine = cPickle.load(fid)

        self.output(filename+" loaded completed!")
        return loaded_machine
