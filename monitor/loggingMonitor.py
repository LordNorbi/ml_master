
import sys
sys.path.append('../')
from monitor import AbstractMonitor
import logging

class LoggingMonitor(AbstractMonitor):
    
    def __init__(self):
        self.logger = logging.getLogger('OutputMonitorLogger')
        self.hdlr = logging.FileHandler('./log/monitor.log')
        #self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        #self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.DEBUG)
        #self.logger_bad = logging.getLogger('BadLogger')
        #self.hdlr_bad = logging.FileHandler('./db/sql_bad.log')
        #self.logger_bad.addHandler(self.hdlr_bad)
        #self.logger_bad.setLevel(logging.DEBUG)
        
    def __taskset_event__(self, taskset):
        pass

    def __taskset_start__(self, taskset):
        pass

    def __taskset_finish__(self, taskset):
        for task in taskset:
            self.logger.info("task: {}".format(task.id))
            for job in task.jobs:
                self.logger.info("{} {}".format(job.start_date, job.end_date))

    def __taskset_stop__(self, taskset):
        for task in taskset:
            task.jobs = []
        pass

#def __taskset_bad__(self, taskset, n):
#self.logger_bad.info('{} tries:\n{}'.format(n, str(taskset)))
#pass


