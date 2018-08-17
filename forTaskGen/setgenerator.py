#this file defines tasksets-generators

from taskgen.taskset import TaskSet
from taskgen.task import Task
from taskgen.blocks import *
import copy

class SetGenerator(TaskSet):
    
    criticaltime = {"criticaltime" : [1000,2000,3000]}
    deadline = {"deadline" : [3000,6000,9000]}
    numberofjobs = {"numberofjobs" : [1,8,16]}
    numberOfVariants = 50
    periods = {"period" : [0,500,10000]}
    priorities = {"priority" : [8,32,128]}

#function ben00 - ben04 define a Taskset-Generator that executes the same Task 100 times with the same configuration. The result of that executuions can be used a kind of a benchmark. So the execution times can be compared and the right values for the attributes can be choosen.
    def ben00(self):
        set = TaskSet([])
        v00 = [0,1000,1000000]
        o00 ={"offset" : [1000]}
        nj00 = {"numberofjobs" : [1,4,16]}
        p00 = {"period" : [5000,10000]}
        pro00 = {"priority" : [8,32,127]}
        d00 = {"deadline" : [12500]}
        
        task00 = Task(hey.Value(v00),o00,nj00,p00,pro00,d00)
        set.append(task00)
        
        return set
    
    def ben01(self):
        set = TaskSet([])
        # Wert mit dem der Task ausgeführt wird
        v00 = [100,1000,10000,100000,1000000]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [100]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8]}
        
        task00 = Task(pi.Value(v00),o00,nj00,p00,pro00)
        set.append(task00)
        return set
    
    def ben02(self):
        set = TaskSet([])
        # Wert mit dem der Task ausgeführt wird
        v00 = [41,42,10041,10042,1000041,1000042]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [100]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8]}
        
        task00 = Task(cond_42.Value(v00),o00,nj00,p00,pro00)
        set.append(task00)
        return set
    
    def ben03(self):
        set = TaskSet([])
        # Wert mit dem der Task ausgeführt wird
        v00 = [100,103,10000,10003,1000000,1000003]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [100]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8]}
        
        task00 = Task(cond_mod.Value(v00),o00,nj00,p00,pro00)
        set.append(task00)
        return set
    
    def ben04(self):
        set = TaskSet([])
        # Wert mit dem der Task ausgeführt wird
        v00 = [10,11,10000,10001,1000000,1000001]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [100]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8]}
        
        task00 = Task(tumatmul.Value(v00),o00,nj00,p00,pro00)
        set.append(task00)
        return set
    
    def finalSetSmall(self):
        # returns a Taskset-Generator with round about 16k TaskSets
        set = TaskSet([])
        #nach dieser Zeit wird der Task beendet
        ct00 = {"criticaltime" : [12000]}#medean execution time of task 0: 1200; 100% at 1650
        ct01 = {"criticaltime" : [16000]}#medean execution time of task 1: 1600;  90% at 2800
        ct02 = {"criticaltime" : [13000]}#medean execution time of task 2: 1300;  90% at 2300
        ct03 = {"criticaltime" : [15000]}#medean execution time of task 3: 1400;  90% at 2700
        ct04 = {"criticaltime" : [30000]}#medean execution time of task 4: 3150;  95% at 3200
        # Wert mit dem der Task ausgeführt wird
        v00 = [0]
        v01 = [100,1000]
        v02 = [42,10041]
        v03 = [10000,10003]
        v04 = [10000,10001]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        o01 ={"offset" : [500]}
        o02 ={"offset" : [500]}
        o03 ={"offset" : [500]}
        o04 ={"offset" : [500]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [1,4]}
        nj01 = {"numberofjobs" : [1,4]}
        nj02 = {"numberofjobs" : [1,4]}
        nj03 = {"numberofjobs" : [1,4]}
        nj04 = {"numberofjobs" : [1,4]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        p01 = {"period" : [10000]}
        p02 = {"period" : [10000]}
        p03 = {"period" : [10000]}
        p04 = {"period" : [10000]}
        #Time zu der der Task "fertig sein soll" wird nur zum skedulen verwendet. Nach Überschreiten der deadline wird der task beednet und darf nur dannw eiter rechnen, wenn kein anderer Task rechnen möchte
        d00 = {"deadline" : [12500]}
        d01 = {"deadline" : [22500]}
        d02 = {"deadline" : [20000]}
        d03 = {"deadline" : [25000]}
        d04 = {"deadline" : [30000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8,127]}
        pro01 = {"priority" : [16,127]}
        pro02 = {"priority" : [64,127]}
        pro03 = {"priority" : [16,127]}
        pro04 = {"priority" : [32,127]}
        
        task00 = Task(hey.Value(v00),ct00,o00,nj00,p00,d00,pro00)
        set.append(task00)
        task01 = Task(pi.Value(v01),ct01,o01,nj01,p01,d01,pro01)
        #set.append(task01)
        set.append(task01)
        task02 = Task(cond_42.Value(v02),ct02,o02,nj02,p02,d02,pro02)
        set.append(task02)
        task03 = Task(cond_mod.Value(v03),ct03,o03,nj03,p03,d03,pro03)
        set.append(task03)
        task04 = Task(tumatmul.Value(v04),ct04,o04,nj04,p04,d04,pro04)

        set.append(task00)
        set.append(task01)
        set.append(task02)
        set.append(task03)
        set.append(task04)
        
        return set
    
    def specialSet(self,setcount):
        #setcount defines how many Tasks are allowed to be in one Taskset.
        #The funtion returns a list of Taskset-Generators.
        
        #each Task gets its own parameters:
        #parameter xxxx00 is for task 0
        #parameter xxxx01 is for task 1
        #parameter xxxx02 is for task 2
        #parameter xxxx03 is for task 3
        #parameter xxxx04 is for task 4
        
        #nach dieser Zeit wird der Task beendet
        ct00 = {"criticaltime" : [12000]}
        ct01 = {"criticaltime" : [18000]}
        ct02 = {"criticaltime" : [13000]}
        ct03 = {"criticaltime" : [15000]}
        ct04 = {"criticaltime" : [30000]}
        # Wert mit dem der Task ausgeführt wird
        v00 = [0]
        v01 = [100,1000]
        v02 = [42,10041]
        v03 = [10000,10003]
        v04 = [10000,10001]
        #Verzögerung des Taskes vor Ausführung
        o00 ={"offset" : [1000]}
        o01 ={"offset" : [500]}
        o02 ={"offset" : [500]}
        o03 ={"offset" : [500]}
        o04 ={"offset" : [500]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [1,4]}
        nj01 = {"numberofjobs" : [1,4]}
        nj02 = {"numberofjobs" : [1,4]}
        nj03 = {"numberofjobs" : [1,4]}
        nj04 = {"numberofjobs" : [1,4]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [10000]}
        p01 = {"period" : [10000]}
        p02 = {"period" : [10000]}
        p03 = {"period" : [10000]}
        p04 = {"period" : [10000]}
        #Time zu der der Task "fertig sein soll" wird nur zum skedulen verwendet. Nach Überschreiten der deadline wird der task beednet und darf nur dannw eiter rechnen, wenn kein anderer Task rechnen möchte
        d00 = {"deadline" : [12500]}
        d01 = {"deadline" : [22500]}
        d02 = {"deadline" : [20000]}
        d03 = {"deadline" : [25000]}
        d04 = {"deadline" : [30000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [8,127]}
        pro01 = {"priority" : [16,127]}
        pro02 = {"priority" : [64,127]}
        pro03 = {"priority" : [16,127]}
        pro04 = {"priority" : [32,127]}
        
        #creates the Task-Generators
        task00 = Task(hey.Value(v00),ct00,o00,nj00,p00,d00,pro00)
        task01 = Task(pi.Value(v01),ct01,o01,nj01,p01,d01,pro01)
        task02 = Task(cond_42.Value(v02),ct02,o02,nj02,p02,d02,pro02)
        task03 = Task(cond_mod.Value(v03),ct03,o03,nj03,p03,d03,pro03)
        task04 = Task(tumatmul.Value(v04),ct04,o04,nj04,p04,d04,pro04)
        
        jobs = []
        
        #creates the "Kreuzprodukt" of the Tasks as Taskset-Generator. But with a maximum of setcount Tasks in each Taskset.
        tasks=(task00,task01,task02,task03,task04)
        i = 0
        if setcount>0 and setcount<5:
            set = TaskSet([])
            while i < 5:
                set0 = copy.deepcopy(set)
                set0.append(copy.deepcopy(tasks[i]))
                if setcount>1:
                    j=i+1
                    while j < 5:
                        set1 = copy.deepcopy(set0)
                        set1.append(copy.deepcopy(tasks[j]))
                        if setcount >2:
                            k=j+1
                            while k < 5:
                                set2 = copy.deepcopy(set1)
                                set2.append(copy.deepcopy(tasks[k]))
                                if setcount >3:
                                    l = k+1
                                    while l < 5:
                                        set3 = copy.deepcopy(set2)
                                        set3.append(copy.deepcopy(tasks[l]))
                                        jobs.append(set3)
                                        l = l+1
                                else:
                                    jobs.append(set2)
                                k = k+1
                        else:
                            jobs.append(set1)
                        j = j+1
                else:
                    jobs.append(set0)
                i = i+1

        set = TaskSet([])
        if setcount==5:
            set.append(task00)
            set.append(task01)
            set.append(task02)
            set.append(task03)
            set.append(task04)
            jobs.append(set)
            return jobs
        return jobs


