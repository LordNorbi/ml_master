import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()
logmon = LoggingMonitor()
set = gen.set05()
dis.add_job(set,logmon)




