from taskgen.taskset import TaskSet
from taskgen.task import Task
from taskgen.blocks import *

class SetGenerator(TaskSet):
    
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
    
    def set01(self):
        set = TaskSet([])
        task01 = Task(hey.Value(0),{"priority" : [16]},{"offset" : [3000]},{"period" : [10000]},{"numberofjobs" : [20]})
        set.append(task01)
        return set
    def set02(self):
        set = TaskSet([])
        task02 = Task(pi.Value(1000),{"priority" : [16]},{"offset" : [3000]},{"period" : [10000]},{"numberofjobs" : [20]})
        set.append(task02)
        return set
    def set03(self):
        set = TaskSet([])
        task02 = Task(cond_42.Value(4200000),{"priority" : [16]},{"offset" : [3000]},{"period" : [10000]},{"numberofjobs" : [20]})
        set.append(task02)
        return set
    def set04(self):
        set = TaskSet([])
        task02 = Task(cond_mod.Value(100001),{"priority" : [16]},{"offset" : [3000]},{"period" : [10000]},{"numberofjobs" : [20]})
        set.append(task02)
        return set
    def set05(self):
        set = TaskSet([])
        task02 = Task(tumatmul.Value(1000000),{"priority" : [16]},{"offset" : [3000]},{"period" : [10000]},{"numberofjobs" : [20]})
        set.append(task02)
        return set
    
    def testset(self):
        set = TaskSet([])
        
        task01 = Task(hey.Value(0))
        set.append(task01)
        task02 = Task(pi.Value(1000))
        set.append(task02)
        task03 = Task(cond_42.Value(4200000))
        set.append(task03)
        task04 = Task(cond_mod.Value(100003))
        set.append(task04)
        task05 = Task(tumatmul.Value(98000))
        set.append(task05)
        
        return set
    
    def finalSet(self):
    
        set = TaskSet([])
        #nach dieser Zeit wird der Task beendet
        ct00 = {"criticaltime" : [4125]}#medean execution time of task 0: 1300; 100% at 1650
        ct01 = {"criticaltime" : [7000]}#medean execution time of task 1: 2300;  90% at 2800
        ct02 = {"criticaltime" : [5750]}#medean execution time of task 2: 2000;  90% at 2300
        ct03 = {"criticaltime" : [6750]}#medean execution time of task 3: 2239;  90% at 2700
        ct04 = {"criticaltime" : [8000]}#medean execution time of task 4: 3027;  95% at 3200
        # Wert mit dem der Task ausgeführt wird
        v00 = {"value" : [0]}
        v01 = {"value" : [1,100,1000]}
        v02 = {"value" : [42,420000,4200000]}
        v03 = {"value" : [100000,100002,100003]}
        v04 = {"value" : [1000,98000]}
        #Verzögerung des Taskes vor Ausführung
        o00 ={"ofset" : [100]}
        o01 ={"ofset" : [0]}
        o02 ={"ofset" : [0]}
        o03 ={"ofset" : [0]}
        o04 ={"ofset" : [0]}
        #Anzahl der wdh. eines Tasks
        nj00 = {"numberofjobs" : [1,64]}
        nj01 = {"numberofjobs" : [1,64]}
        nj02 = {"numberofjobs" : [1,64]}
        nj03 = {"numberofjobs" : [1,64]}
        nj04 = {"numberofjobs" : [1,64]}
        # nach dieser Zeit wird die nächste instanz des tasks gestartet wenn numberofjobs > 1. dabei wird die "alte" instanz beendet
        p00 = {"period" : [26000]}
        p01 = {"period" : [46000]}
        p02 = {"period" : [41000]}
        p03 = {"period" : [51000]}
        p04 = {"period" : [61000]}
        #Time zu der der Task "fertig sein soll" wird nur zum skedulen verwendet. Nach Überschreiten der deadline wird der task beednet und darf nur dannw eiter rechnen, wenn kein anderer Task rechnen möchte
        d00 = {"deadline" : [25000]}
        d01 = {"deadline" : [45000]}
        d02 = {"deadline" : [40000]}
        d03 = {"deadline" : [50000]}
        d04 = {"deadline" : [60000]}
        #Wenn ein Task eine Priority hat, wird er nach dieser gescheduled, nicht nach der deadline. Deadline ist dann egal. Erst priority danach deadlines
        pro00 = {"priority" : [16,128]}
        pro01 = {"priority" : [32,128]}
        pro02 = {"priority" : [16,128]}
        pro03 = {"priority" : [32,128]}
        pro04 = {"priority" : [16,128]}
        
        task00 = Task(hey.Value(v00), ct00,o00,nj00,p00,d00,pro00)
        set.append(task00)
        task01 = Task(pi.Value(v01), ct01,o01,nj01,p01,d01,pro01)
        set.append(task01)
        task02 = Task(cond_42.Value(v02), ct02,o02,nj02,p02,d02,pro02)
        set.append(task02)
        task03 = Task(cond_mod.Value(v03), ct03,o03,nj03,p03,d03,pro03)
        set.append(task03)
        task04 = Task(tumatmul.Value(v04), ct04,o04,nj04,p04,d04,pro04)
        set.append(task04)
        
        return set
    
    
    def returnrobert(self):
        
        set = TaskSet([])
        
        task01 = Task(hey.Value(1), period.HighRandom(), priority.HighRandom())
        set.append(task01)
        task02 = Task(pi.Variants(self.numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task03)
        task04 = Task(cond_mod.Variants(self.numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task04)
        task05 = Task(linpack.Variants(self.numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task05)
        
        return set
    
    
    def size2(self):
        
        set = TaskSet([])
        
        task02 = Task(pi.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs,)
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task03)
        
        return set
    
    
    def size3(self):
        
        set = TaskSet([])
        
        task02 = Task(pi.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task03)
        task04 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task04)
        
        return set
    
    
    def size4(self):
        
        set = TaskSet([])
        numberOfVariants = 50
        priorities = {"priority" : [8,16,32,64,128]}
        periods = {"period" : [0,500,10000]}
        
        task02 = Task(pi.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task03)
        task04 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task04)
        task05 = Task(linpack.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task05)
        
        return set
    
    
    def size5(self):
        
        set = TaskSet([])
        
        task02 = Task(pi.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task03)
        task04 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task04)
        task05 = Task(linpack.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task05)
        task06 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task06)
        
        return set
    
    def size6(self):
        
        set = TaskSet([])
        
        task02 = Task(pi.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task02)
        task03 = Task(cond_42.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task03)
        task04 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task04)
        task05 = Task(linpack.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task05)
        task06 = Task(cond_mod.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task06)
        task07 = Task(linpack.Variants(self.numberOfVariants),self.criticaltime, self.deadline, self.periods, self.priorities, self.numberofjobs)
        set.append(task07)
        
        return set



