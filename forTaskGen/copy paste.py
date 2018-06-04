import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()

set = gen.finalSetSmall()
setvar = set.variants()
print(len(list(setvar)))


sqlmon = SQLMonitor()
dis.add_job(set,sqlmon)


logmon = LoggingMonitor()

