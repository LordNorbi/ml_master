import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()

from taskgen.setgenerator2 import SetGenerator2
gen2 = SetGenerator2()
for a in range(1,5):
    list1 = gen2.specialSet(a)
    for l in list1:
        setvar = l.variants()
        #print(len(list(setvar)))
        dis.add_job(l,sqlmon)




