import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
#from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()
#logmon = LoggingMonitor()

#set = gen.ben00()
#dis.add_job(set,logmon)


#bigset = gen.finalSetSmall()
#dis.add_job(bigset,sqlmon)
gen = SetGenerator()
for a in range(0,5):
    list1 = gen.specialSet(a)
    for l in list1:
        setvar = l.variants()
        #print(len(list(setvar)))
        dis.add_job(l,sqlmon)

5 tries:
[
 {'deadline': 12500, 'config': {'arg1': 0}, 'offset': 1000, 'priority': 8, 'quota': '10M', 'numberofjobs': 1, 'period': 10000, 'criticaltime': 12000, 'pkg': 'hey', 'id': 0},
 {'deadline': 22500, 'config': {'arg1': 100}, 'offset': 500, 'priority': 16, 'quota': '10M', 'numberofjobs': 1, 'period': 10000, 'criticaltime': 18000, 'pkg': 'pi', 'id': 1},
 {'deadline': 20000, 'config': {'arg1': 42}, 'offset': 500, 'priority': 64, 'quota': '10M', 'numberofjobs': 1, 'period': 10000, 'criticaltime': 13000, 'pkg': 'cond_42', 'id': 2},
 {'deadline': 25000, 'config': {'arg1': 10000}, 'offset': 500, 'priority': 16, 'quota': '10M', 'numberofjobs': 1, 'period': 10000, 'criticaltime': 15000, 'pkg': 'cond_mod', 'id': 3},
 {'deadline': 30000, 'config': {'arg1': 10000}, 'offset': 500, 'priority': 32, 'quota': '10M', 'numberofjobs': 1, 'period': 10000, 'criticaltime': 30000, 'pkg': 'tumatmul', 'id': 4}]



