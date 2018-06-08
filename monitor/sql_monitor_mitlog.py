from monitor import AbstractMonitor
import os, sqlite3
import logging
import time
import sys
#Monitor for sqlite3


class SQLMonitor(AbstractMonitor):
    """Stores task-sets and events to a SQLite3 DB
    """
    db_name = "db/"+"monitor_data"+".db"
    #db_connection = None
    
    #if db not found, create new one
    def getDB(self):
        #print(self.db_name+" Databasefile created an ready to use.")
        if not os.path.exists(self.db_name):
            db_connection = sqlite3.connect(self.db_name,check_same_thread=False)
            #create tables in db
            db_cursor = db_connection.cursor()
            sqlTaskSet = "CREATE TABLE IF NOT EXISTS TaskSet (Set_ID INTEGER PRIMARY KEY,Exit_Value INT)"
            sqlTask = "CREATE TABLE IF NOT EXISTS Task (Task_ID INTEGER, Set_ID INTEGER, Priority INT, Deadline INT, Quota STRING, PKG STRING, Arg INT, Period INT, Number_of_Jobs INT, Offset INT, PRIMARY KEY (Task_ID, Set_ID))"
            sqlJob = "CREATE TABLE IF NOT EXISTS Job (Job_ID INTEGER, Task_ID INTEGER, Set_ID INTEGER, Start_Date INT, End_Date INT, Exit_Value STRING, PRIMARY KEY (Job_ID, Task_ID, Set_ID))"
            db_cursor.execute(sqlTaskSet)
            db_cursor.execute(sqlTask)
            db_cursor.execute(sqlJob)
            db_connection.commit()
            db_connection.close()
        
    def __init__(self):
        self.getDB()
        self.logger = logging.getLogger('OutputMonitorLogger')
        self.hdlr = logging.FileHandler('./db/sql.log')
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.DEBUG)

    def __taskset_event__(self, taskset):
        pass

    def __taskset_start__(self, taskset):
        pass

    def __taskset_finish__(self, taskset):
        notyetcommited = True
        while notyetcommited:
            try:
                db_connection = sqlite3.connect(self.db_name,check_same_thread=False)
                db_cursor = db_connection.cursor()
                sqlSet = "Insert into TaskSet  (Exit_Value) Values (0)"
                db_cursor.execute(sqlSet)
        #id of the created TaskSet
                set_ID = db_cursor.lastrowid
                db_connection.commit()
               # db_connection.close()
                notyetcommited = False
            except:
                print("1 A DB Exception occured. Please wait a second, I try to fix it...")

        for task in taskset:
            #print("task:")
            #print(task)
            #print("priority" in task.keys())
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
            
            #db_cursor.execute(sqlTask)
            notyescommited = True
            while notyetcommited:
                try:
                #    db_connection = sqlite3.connect(self.db_name,check_same_thread=False)
                #    db_cursor = db_connection.cursor()
                    db_cursor.execute(sqlTask)
                    db_connection.commit()
                #    db_connection.close()
                    notyetcommited = False
                except:
                    print("2 An DB Exception occured. Pls wait a second I try to fix it...")
            #db_connection.commit()
            
           # succesfull = -1 #if the job exited succesfully or not -1 = not succesfull, +1= succesfull
            #loops through the jobs of a task and adds the information to the db
            job_id = 0
            for job in task.jobs:
                #succesfull = -1
                #if job.exit_value == "EXIT":  #if EXIT then job ended succesfully
                   # succesfull = 1
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

                notyetcommited = True
                while notyetcommited:
                    try:
                 #       db_connection = sqlite3.connect(self.db_name,check_same_thread=False)
                        db_cursor = db_connection.cursor()
                        db_cursor.execute(sqlJob)
                #print("Statement:")
                        #self.logger.info(sqlJob)
                        db_connection.commit()
                 #       db_connection.close()
                        notyetcommited = False
                    except:
                        print("error",sys.exc_info()[0])
                        print("3 A DB Exception occured. Please wait a moment so I can try to fix it...")
                        time.sleep(5)

            db_connection.close()
  
    def __taskset_stop__(self, taskset):
        pass
