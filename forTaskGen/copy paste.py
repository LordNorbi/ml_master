import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor
dis = Distributor()
gen = SetGenerator()
logmon = LoggingMonitor()
set = gen.set01()
dis.add_job(set,logmon)




