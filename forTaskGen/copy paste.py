import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()

bigset = gen.finalSetSmall()
#dis.add_job(bigset,sqlmon)
gen = SetGenerator()
for a in range(4,0,-1):
    list1 = gen.specialSet(a)
    for l in list1:
        setvar = l.variants()
        #print(len(list(setvar)))
        dis.add_job(l,sqlmon)




