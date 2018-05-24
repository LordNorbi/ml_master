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
    
    def final(self):
    
        set = TaskSet([])
        ct00 = {"criticaltime" : [0]}
        ct01 = {"criticaltime" : [0]}
        ct02 = {"criticaltime" : [0]}
        ct03 = {"criticaltime" : [0]}
        ct04 = {"criticaltime" : [0]}
        
        v00 = {"value" : [0]}
        v01 = {"value" : [1,10,100,1000]}
        v02 = {"value" : [42,42000,420000,4200000]}
        v03 = {"value" : [100000,100001,100002,100003]}
        v04 = {"value" : [1000,10000,98000]}
        
        o00 ={"ofset" : [100]}
        o01 ={"ofset" : [0]}
        o02 ={"ofset" : [0]}
        o03 ={"ofset" : [0]}
        o04 ={"ofset" : [0]}
        
        nj00 = {"numberofjobs" : [1,32,128]}
        nj01 = {"numberofjobs" : [1,32,128]}
        nj02 = {"numberofjobs" : [1,32,128]}
        nj03 = {"numberofjobs" : [1,32,128]}
        nj04 = {"numberofjobs" : [1,32,128]}
        
        p00 = {"period" : [0]}
        p01 = {"period" : [0]}
        p02 = {"period" : [0]}
        p03 = {"period" : [0]}
        p04 = {"period" : [0]}
        
        d00 = {"deadline" : [0]}
        d01 = {"deadline" : [0]}
        d02 = {"deadline" : [0]}
        d03 = {"deadline" : [0]}
        d04 = {"deadline" : [0]}
        
        pro00 = {"priority" : [16,32,128,128]}
        pro01 = {"priority" : [16,32,128,128]}
        pro02 = {"priority" : [16,32,128,128]}
        pro03 = {"priority" : [16,32,128,128]}
        pro04 = {"priority" : [16,32,128,128]}
        
        task00 = Task(hey.Value(v00), ct00,o00,nj00,p00,d00,pro00)
        set.append(task00)
        task01 = Task(pi.Variants(v01), ct01,o01,nj01,p01,d01,pro01)
        set.append(task01)
        task02 = Task(cond_42.Variants(v02), ct02,o02,nj02,p02,d02,pro02)
        set.append(task02)
        task03 = Task(cond_mod.Variants(v03), ct03,o03,nj03,p03,d03,pro03)
        set.append(task03)
        task04 = Task(tumatmul.Variants(v04), ct04,o04,nj04,p04,d04,pro04)
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



