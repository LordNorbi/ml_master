from monitor import AbstractMonitor
import os, sqlite3

#Monitor for sqlite3


class SQLMonitor(AbstractMonitor):
    """Stores task-sets and events to a SQLite3 DB
    """
    db_name = "db/"+"monitor_data"+".db"
    db_connection = None
    
    #if db not found, create new one
    def getDB(self):
        #print("--------------"+self.db_name)
        if not os.path.exists(self.db_name):
            self.db_connection = sqlite3.connect(self.db_name)
            #create tables in db
            db_cursor = self.db_connection.cursor()
            sqlTaskSet = "CREATE TABLE IF NOT EXISTS TaskSet (Set_ID INTEGER PRIMARY KEY,Exit_Value INT)"
            sqlTask = "CREATE TABLE IF NOT EXISTS Task (Task_ID INTEGER, Set_ID INTEGER, Priority INT, Deadline INT, Quota STRING, PKG STRING, Arg INT, Period INT, Number_of_Jobs INT, Offset INT, PRIMARY KEY (Task_ID, Set_ID))"
            sqlJob = "CREATE TABLE IF NOT EXISTS Job (Job_ID INTEGER, Task_ID INTEGER, Set_ID INTEGER, Start_Date INT, End_Date INT, Exit_Value INT, PRIMARY KEY (Job_ID, Task_ID, Set_ID))"
            db_cursor.execute(sqlTaskSet)
            db_cursor.execute(sqlTask)
            db_cursor.execute(sqlJob)
            self.db_connection.commit()
            self.db_connection.close()
    

    def __init__(self):
        self.getDB()

    def __taskset_event__(self, taskset):
        pass

    def __taskset_start__(self, taskset):
        pass

    def __taskset_finish__(self, taskset):
        self.db_connection = sqlite3.connect(self.db_name)
        db_cursor = self.db_connection.cursor()
        sqlSet = "Insert into TaskSet  (Exit_Value) Values (0)"
        db_cursor.execute(sqlSet)
        #id of the created TaskSet
        set_ID = db_cursor.lastrowid
        self.db_connection.commit()
        
        for task in taskset:
            #print("task:")
            print(task)
            #print("priority" in task.keys())
            #create the Task with its information
            deadline = -1
            if task["deadline"]!="None":
                deadline = task["deadline"]
            priority = -1
            if task["priority"]!="None":
                deadline = task["priority"]
        
            sqlTask = "Insert into Task (Task_ID, Set_ID, Priority, Deadline, Quota, PKG, Arg, Period, Number_of_Jobs, Offset) Values ({},{},{},{},'{}','{}',{},{},{},{})".format(task.id, set_ID, priority, deadline, task["quota"], task["pkg"], task["config"]["arg1"], task["period"], task["numberofjobs"], task["offset"])
            #print(sqlTask)
            db_cursor.execute(sqlTask)
            self.db_connection.commit()
            
            succesfull = -1 #if the job exited succesfully or not -1 = not succesfull, +1= succesfull
            #loops through the jobs of a task and adds the information to the db
            job_id = 0
            for job in task.jobs:
                if job.exit_value == "EXIT":  #if EXIT then job ended succesfully
                    succesfull = 1
                endtime = -1
                if job.end_date!="None":
                    endtime = job.end_date
                sqlJob = "Insert into Job (Job_ID, Task_ID, Set_ID, Start_Date, End_Date, Exit_Value) Values ({},{},{},{},{},{})".format(job_id, task.id, set_ID, job.start_date, endtime, succesfull)
                job_id = job_id+1;
                db_cursor.execute(sqlJob)
                print("Statement:")
                print(sqlJob)
                self.db_connection.commit()

    def __taskset_stop__(self, taskset):
        pass
