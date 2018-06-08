import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()

set1 = gen.specialSet(1)
setvar = set1.variants()
print(len(list(setvar)))

set2 = gen.specialSet(2)
setvar = set2.variants()
print(len(list(setvar)))

set3 = gen.specialSet(3)
setvar = set3.variants()
print(len(list(setvar)))

set4 = gen.specialSet(4)
setvar = set4.variants()
print(len(list(setvar)))


dis.add_job(set1,sqlmon)
dis.add_job(set2,sqlmon)
dis.add_job(set3,sqlmon)
dis.add_job(set4,sqlmon)


