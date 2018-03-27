from monitor import AbstractMonitor
import os, sqlite3

"""Monitor for sqlite3
"""

class SQLMonitor(AbstractMonitor):
    """Stores task-sets and events to a SQLite3 DB
    """
    db_name = "../db/"+"monitor_data"+".db"
    db_connection = None
    task_attribute = ["SetId","TaskId","Priority","pkg","quota","start","end"]
    task_types_of_attributes = ["INT","INT","INT","INT","INT","STRING","STRING"] #Booleans are stores as INT (0 or 1)
    set_attribute = ["SetId","Time","result"]
    set_types_of_attributes = ["INT","String","INT"] #Booleans are stores as INT (0 or 1)

    def __init__(self):
        self.checkDB()
        #client = MongoClient(uri)
        #self.database = client['tasksets']

    def __taskset_event__(self, taskset):
        pass

    def __taskset_start__(self, taskset):
        pass

    def __taskset_finish__(self, taskset):
        setData = []
        self.insertSet(setData)
        for task in taskset:
            jobs_func = lambda job : {
                'start_date' : job.start_date,
                'end_date' : job.end_date
            }
            taskData = []
            self.insertTask(taskData)
            # insert description & jobs of task to db
            self.database.taskset.task.insert_one({
                'description' : task,
                'jobs' : list(map(jobs_func, task.jobs))
            })

    def __taskset_stop__(self, taskset):
        pass




    def checkDB(self):
        if not os.path.exists(self.db_name):
            print "Datenbank "+self.db_name+" nicht vorhanden - Datenbank wird anglegt."
            self.createDB()
            return()
        self.db_connection = sqlite3.connect(self.db_name)
        print("Datenbank "+self.db_name+" found!")
        print(self.db_name+" contains "+str(self.getNumberOfEntries())+" entries")

    def createDB(self):
    #create new db

        self.db_connection = sqlite3.connect(self.db_name)
        print("DB created!")
        self.createTables()

    def createTables(self):

        db_cursor = self.db_connection.cursor()

        #Check if Attributes and Types maches (Task)
        if len(self.task_attribute)!= len(self.task_types_of_attributes):
            print("Missmatch Attribute and Types (Task)! EXIT")
            return()
        #Check if Attributes and Types maches (Set)
        if len(self.set_attribute)!= len(self.set_types_of_attributes):
            print("Missmatch Attribute and Types(Set)! EXIT")
            return()

        #create the TASK Table
        sql = "CREATE TABLE IF NOT EXISTS Task("
        for i in range(len(self.task_attribute)):
            if i!=0:
                sql+=","+self.task_attribute[i]+" "+self.task_types_of_attributes[i]
            else:
                sql+=self.task_attribute[i]+" "+self.task_types_of_attributes[i]

        sql+=")"
        db_cursor.execute(sql)
        self.db_connection.commit()

        print("Table "+self.db_name+" mit "+ sql +" angelegt")

        #create the SET Table
        sql = "CREATE TABLE IF NOT EXISTS Set("
        for i in range(len(self.set_attribute)):
            if i!=0:
                sql+=","+self.set_attribute[i]+" "+self.set_types_of_attributes[i]
            else:
                sql+=self.set_attribute[i]+" "+self.set_types_of_attributes[i]

        sql+=")"
        db_cursor.execute(sql)
        self.db_connection.commit()

        print("Table "+self.db_name+" mit "+ sql +" angelegt")


        return()

    def getNumberOfEntries(self):
        sql = "SELECT count(Id) FROM Set where Id >= 0"
        db_cursor = self.db_connection.cursor()
        db_cursor.execute(sql)
        return db_cursor.fetchone()[0]

    def insertSet(self,tup):
        if (len(self.set_attr)-1)!= len(tup):
            print("Missmatch at Insertion (Set). EXIT")
            return()

        sql = "INSERT INTO Set("
        for j in range(len(self.set_attr)):
            if j!=0:
                sql+=","+self.set_attr[j]
            else:
                sql+=self.set_attr[j]

        sql+=")VALUES("


        for i in range(len(tup)):
            if i!=0:
                sql+=","+str(tup[i])
            else:
                sql+=str(id)+","+str(tup[i])
        sql+=")"
        #print sql
        db_cursor = self.db_connection.cursor()
        db_cursor.execute(sql)
        self.db_connection.commit()

    def insertTask(self,tup):
        if (len(self.task_attr)-1)!= len(tup):
            print("Missmatch at Insertion (Task). EXIT")
            return()

        sql = "INSERT INTO Task("
        for j in range(len(self.task_attr)):
            if j!=0:
                sql+=","+self.task_attr[j]
            else:
                sql+=self.task_attr[j]

        sql+=")VALUES("


        for i in range(len(tup)):
            if i!=0:
                sql+=","+str(tup[i])
            else:
                sql+=str(id)+","+str(tup[i])
        sql+=")"
        #print sql
        db_cursor = self.db_connection.cursor()
        db_cursor.execute(sql)
        self.db_connection.commit()
