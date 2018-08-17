#this file can bei copy pasted into a python consol started in the distributor directory.
#It generates a distributor, a monitor and the tasksets. it also adds the taskst to the distributor.
# After the code in this file the distributor can be configured with its function (set_max_machine_value(20) etc.

import sys
sys.path.append('../')
from distributor import Distributor
from taskgen.setgenerator import SetGenerator

from monitors.sql_monitor import SQLMonitor
dis = Distributor()
gen = SetGenerator()
sqlmon = SQLMonitor()

#creates the generator with Tasksets consiting of 1 up to 5 Tasks
#adds them with add_job to the job_queue of the distributor
for a in range(1,6):
    list1 = gen.specialSet(a)
    for l in list1:
        setvar = l.variants()
        print(len(list(setvar))) #prints the length of the Taskset
        dis.add_job(l,sqlmon)

