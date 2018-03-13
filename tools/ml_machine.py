import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import svm
from matplotlib.cbook import Null
from sklearn.model_selection import train_test_split

class ml_machine:
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    svm_poly = None
    dec_tree = None
    k_nearest = None
    logist_reg = None
    naive_bay = None

    def __init__(self, X_data, y_data, split=0.25):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_data, y_data, test_size=split, random_state=0)

    def output(self, msg):
        for line in msg.splitlines():
            print "ML: "+line

    def createSVM_poly(self):
        start = time.time()
        self.svm_poly=svm.SVC(kernel='poly', degree=2,cache_size=7000, tol=0.0001, class_weight={1: 20}, C=1)
        self.svm_poly.fit(self.input_2dvector, self.output_1dvector)
        end = time.time()
        self.output("SVM poly done in: " +  str(end - start) + " s")
        return()

    def createDEC_tree(self):

        return()

    def createK_nearest(self):

        return()

    def createLOGIST_reg(self):

        return()

    def createNAIVE_bay(self):

        return()
