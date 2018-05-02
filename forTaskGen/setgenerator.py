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



