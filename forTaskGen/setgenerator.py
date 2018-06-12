from taskgen.taskset import TaskSet
from taskgen.task import Task
from taskgen.blocks import *
import copy

class SetGenerator2(TaskSet):
    
    criticaltime = {"criticaltime" : [1000,2000,3000]}
    deadline = {"deadline" : [3000,6000,9000]}
    numberofjobs = {"numberofjobs" : [1,8,16]}
    numberOfVariants = 50
    periods = {"period" : [0,500,10000]}
    priorities = {"priority" : [8,32,128]}
    
    #just commt out if it'S to much or reduce numberOfVariants
    # Hey           =     1
    # Pi            =    10
    # cond_42       =    10
    # cond_mod      =    10
    # linpack       =    10
    # ---------------------
    # 1^10^10^10^10 = 10000
    
    #for even more Tasksets replace HighRandom() with Variants() then not only 1 Value is used but all possible values (at period and at priority possible)
    #or add even more Tasks
    
    
    def finalSetSmall(self):
        # returns round about 16k Sets
        set = TaskSet([])
        #nach dieser Zeit wird der Task beendet
        ct00 = {"criticaltime" : [28125]}#medean execution time of task 0: 1300; 100% at 1650
        ct01 = {"criticaltime" : [34000]}#medean execution time of task 1: 2300;  90% at 2800
        ct02 = {"criticaltime" : [30750]}#medean execution time of task 2: 2000;  90% at 2300
        ct03 = {"criticaltime" : [32750]}#medean execution time of task 3: 2239;  90% at 2700
        ct04 = {"criticaltime" : [36000]}#medean execution time of task 4: 3027;  95% at 3200
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
        pro00 = {"priority" : [8,128]}
        pro01 = {"priority" : [16,128]}
        pro02 = {"priority" : [64,128]}
        pro03 = {"priority" : [16,128]}
        pro04 = {"priority" : [32,128]}
        
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
        set.append(task04)
        
        return set
    
    def specialSet(self,setcount):
        
        #nach dieser Zeit wird der Task beendet
        ct00 = {"criticaltime" : [28125]}#medean execution time of task 0: 1300; 100% at 1650
        ct01 = {"criticaltime" : [34000]}#medean execution time of task 1: 2300;  90% at 2800
        ct02 = {"criticaltime" : [30750]}#medean execution time of task 2: 2000;  90% at 2300
        ct03 = {"criticaltime" : [32750]}#medean execution time of task 3: 2239;  90% at 2700
        ct04 = {"criticaltime" : [36000]}#medean execution time of task 4: 3027;  95% at 3200
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
        pro00 = {"priority" : [8,128]}
        pro01 = {"priority" : [16,128]}
        pro02 = {"priority" : [64,128]}
        pro03 = {"priority" : [16,128]}
        pro04 = {"priority" : [32,128]}
        
        task00 = Task(hey.Value(v00),ct00,o00,nj00,p00,d00,pro00)
        task01 = Task(pi.Value(v01),ct01,o01,nj01,p01,d01,pro01)
        task02 = Task(cond_42.Value(v02),ct02,o02,nj02,p02,d02,pro02)
        task03 = Task(cond_mod.Value(v03),ct03,o03,nj03,p03,d03,pro03)
        task04 = Task(tumatmul.Value(v04),ct04,o04,nj04,p04,d04,pro04)
        
        jobs = []
        tasks=(task00,task01,task02,task03,task04)
        i = 0
        if setcount>0 and setcount<5:
            set = TaskSet([])
            #set = []
            while i < 5:
                set0 = copy.deepcopy(set)
                set0.append(tasks[i])
                #set0.append(i)
                if setcount>1:
                    j=i+1
                    while j < 5:
                        set1 = copy.deepcopy(set0)
                        set1.append(tasks[j])
                        #set1.append(j)
                        if setcount >2:
                            k=j+1
                            while k < 5:
                                set2 = copy.deepcopy(set1)
                                set2.append(tasks[k])
                                #set2.append(k)
                                if setcount >3:
                                    l = k+1
                                    while l < 5:
                                        set3 = copy.deepcopy(set2)
                                        set3.append(tasks[l])
                                        #set3.append(l)
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
        if setcount==5:
            set.append(task00)
            set.append(task01)
            set.append(task02)
            set.append(task03)
            set.append(task04)
            jobs.append(set)
            return jobs
        return jobs


