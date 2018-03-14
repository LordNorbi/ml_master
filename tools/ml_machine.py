import time
import datetime
import cPickle
from sklearn import svm
from sklearn import metrics
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from machine import machine


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

    def __init__(self, X_data, y_data, amount_of_data, split=0.25):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_data, y_data, test_size=split, random_state=0)

    def output(self, msg):
        for line in msg.splitlines():
            print "ML: "+line

    def createSVM_poly(self):
        self.svm_pol = machine
        self.svm_pol.name = "SVM_pol"
        start = time.time()
        self.svm_pol.unfitted = svm.SVC(kernel='poly', degree=2,cache_size=7000, tol=0.0001, class_weight={1: 20}, C=1)
        self.svm_pol.fitted = self.svm_pol.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.svm_pol.duration = end - start
        self.output("SVM poly done in: " +  str(self.svm_pol.duration) + " s")
        return()

    def createDEC_tree(self, max_depth = 3, min_samples_leaf = 5):
        self.dec_tree = machine
        self.dec_tree.name="DEC_tree"
        start = time.time()
        self.dec_tree.unfitted = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth, min_samples_leaf= min_samples_leaf )
        self.dec_tree.fitted = self.dec_tree.unfitted.fit(self.X_train,self.y_train)
        end = time.time()
        self.dec_tree.duration = end - start
        self.output("Dec Tree done in: " +  str(self.dec_tree.duration) + " s")

        return()

    def createK_nearest(self,neighbors = 3):
        self.k_nearest = machine
        self.k_nearest.name = "k_nearest"
        start = time.time()
        self.k_nearest.unfitted = KNeighborsClassifier(n_neighbors=neighbors)
        self.k_nearest.fitted = self.k_nearest.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.k_nearest.duration = end - start
        self.output("k-nearest done in: " +  str(self.k_nearest.duration) + " s")

        return()

    def createLOGIST_reg(self, c=1e5):
        self.logist_reg = machine
        self.logist_reg.name = "logist_reg"
        start = time.time()
        self.logist_reg.unfitted = linear_model.LogisticRegression(C=c)
        self.logist_reg.fitted = self.k_nearest.unfitted.fit(self.X_train, self.y_train)
        end = time.time()
        self.logist_reg.duration = end - start
        self.output("logistc_reg done in: " +  str(self.logist_reg.duration) + " s")

        return()

    def createNAIVE_bay(self):

        return()

    def bench(self,machine):
        if machine == None:
            self.output("There is no SVM to benchmark!")
            return()

        machine.score = machine.fitted.score(self.X_test,self.y_test)
        print "Score: ", machine.score

        y_pred = machine.fitted.predict(self.X_test)
        report = metrics.classification_report(self.y_test, y_pred)

        list=report.encode('ascii','ignore').split()

        machine.precision = float(list[5]), float(list[10]), float(list[17])
        machine.recall = float(list[6]), float(list[11]), float(list[18])
        machine.f1 = float(list[7]), float(list[12]), float(list[19])
        machine.support = float(list[8]), float(list[18]), float(list[20])

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
        sql = "Insert into Machines (Id, Name, Precision_0, Recall_0, F1_0, Support_0, Precision_1, Recall_1, F1_1, Support_1, Duration, Time, Object) VALUES ("
        sql += str(id)+",'"+machine.name+"',"\
               +str(machine.precision[0])+","+ str(machine.recall[0])+","+str(machine.f1[0])+","+str(machine.support[0])+","\
               +str(machine.precision[1])+","+ str(machine.recall[1])+","+str(machine.f1[1])+","+str(machine.support[1])+","\
               +str(machine.duration)+",'"+timestamp+"','"+filename+"')"

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
