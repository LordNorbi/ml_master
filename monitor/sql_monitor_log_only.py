from monitor import AbstractMonitor
import os, sqlite3
import logging
import time
import sys
from threading import Thread, Lock
#Monitor for sqlite3

class Counter():
    i = 0

class SQLMonitor(AbstractMonitor):
    """Stores task-sets and events to a SQLite3 DB
        """
    db_name = "db/"+"monitor_data"+".db"
    setnumber = Counter()
    mutex = Lock()

def __init__(self):

    self.logger = logging.getLogger('OutputMonitorLogger')
    self.hdlr = logging.FileHandler('./db/sql.log')
    self.formatter = logging.Formatter('%(asctime)s %(message)s')
    self.hdlr.setFormatter(self.formatter)
    self.logger.addHandler(self.hdlr)
    self.logger.setLevel(logging.DEBUG)
    
    def __taskset_event__(self, taskset):
        pass
    
    def __taskset_start__(self, taskset):
        pass
    
    def __taskset_finish__(self, taskset):
        
        set_ID = -1
        self.mutex.acquire()
        try:
            set_ID = self.setnumber.i
            Counter.i = set_ID + 1
        finally:
            self.mutex.release()
        sqlSet = "Insert into TaskSet  (Set_ID, Exit_Value) Values ("+set_ID+", 0)"
        self.logger.info(sqlSet)
        
        for task in taskset:
            
            #create the Task with its information
            deadline = -1
            if task["deadline"]!="None":
                deadline = task["deadline"]
            priority = -1
            if task["priority"]!="None":
                priority = task["priority"]
            period = -1
            if task["period"]!="None":
                period = task["period"]
            
            if period == None:
                period = -1
            if priority == None:
                priority = -1
            if deadline == None:
                deadline = -1
            
            sqlTask = "Insert into Task (Task_ID, Set_ID, Priority, Deadline, Quota, PKG, Arg, Period, Number_of_Jobs, Offset) Values ({},{},{},{},'{}','{}',{},{},{},{})".format(task.id, set_ID, priority, deadline, task["quota"], task["pkg"], task["config"]["arg1"], period, task["numberofjobs"], task["offset"])
            self.logger.info(sqlTask)
            
            job_id = 0
            for job in task.jobs:
                
                endtime = -1
                if job.end_date!="None":
                    endtime = job.end_date
                starttime = -1
                if job.start_date!="None":
                    starttime = job.start_date
                
                if endtime == None:
                    endtime = -1
                if starttime == None:
                    starttime = -1
                
                exit_value = "None"
                if job.exit_value != None:
                    exit_value = job.exit_value
                sqlJob = "Insert into Job (Job_ID, Task_ID, Set_ID, Start_Date, End_Date, Exit_Value) Values ({},{},{},{},{},{})".format(job_id, task.id, set_ID, starttime, endtime, "'"+exit_value+"'")
                job_id = job_id+1;
                        self.logger.info(sqlJob)

def __taskset_stop__(self, taskset):
    pass
