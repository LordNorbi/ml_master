from taskset import TaskSet
from task import Task
from blocks import *

class SetGenerator(TaskSet):
    numberOfVariants = 2                                #50
    priorities = {"priority" : [16,64]}                 #[8,16,32,64,128]
    periods = {"period" : [0,5]}                        #[0,5,10]
    
    def returnrobert(self):
        
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
        
        set = TaskSet([])
        numberOfVariants = 10
        
        task01 = Task(hey.HelloWorld, period.HighRandom(), priority.HighRandom())
        set.append(task01)
        task02 = Task(pi.Variants(numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task03)
        task04 = Task(cond_mod.Variants(numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task04)
        task05 = Task(linpack.Variants(numberOfVariants), period.HighRandom(), priority.HighRandom())
        set.append(task05)
        
        return set
    
    
    def size2(self):
        
        set = TaskSet([])
        numberOfVariants = self.numberOfVariants
        priorities = self.priorities
        periods = self.periods
        
        task02 = Task(pi.Variants(numberOfVariants), periods, priorities)
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), periods, priorities)
        set.append(task03)
        
        return set
    
    
    def size3(self):
        
        set = TaskSet([])
        numberOfVariants = self.numberOfVariants
        priorities = self.priorities
        periods = self.periods
        
        task02 = Task(pi.Variants(numberOfVariants), periods, priorities)
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), periods, priorities)
        set.append(task03)
        task04 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task04)
        
        return set
    
    
    def size4(self):
        
        set = TaskSet([])
        numberOfVariants = self.numberOfVariants
        priorities = self.priorities
        periods = self.periods
        
        task02 = Task(pi.Variants(numberOfVariants), periods, priorities)
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), periods, priorities)
        set.append(task03)
        task04 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task04)
        task05 = Task(linpack.Variants(numberOfVariants), periods, priorities)
        set.append(task05)
        
        return set
    
    
    def size5(self):
        
        set = TaskSet([])
        numberOfVariants = self.numberOfVariants
        priorities = self.priorities
        periods = self.periods
        
        task02 = Task(pi.Variants(numberOfVariants), periods, priorities)
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), periods, priorities)
        set.append(task03)
        task04 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task04)
        task05 = Task(linpack.Variants(numberOfVariants), periods, priorities)
        set.append(task05)
        task06 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task06)
        
        return set
    
    def size6(self):
        
        set = TaskSet([])
        numberOfVariants = self.numberOfVariants
        priorities = self.priorities
        periods = self.periods
        
        task02 = Task(pi.Variants(numberOfVariants), periods, priorities)
        set.append(task02)
        task03 = Task(cond_42.Variants(numberOfVariants), periods, priorities)
        set.append(task03)
        task04 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task04)
        task05 = Task(linpack.Variants(numberOfVariants), periods, priorities)
        set.append(task05)
        task06 = Task(cond_mod.Variants(numberOfVariants), periods, priorities)
        set.append(task06)
        task07 = Task(linpack.Variants(numberOfVariants), periods, priorities)
        set.append(task07)
        
        return set
    
    def getPossibilities(self, taskset):
        
        setgen = taskset.variants()
        
        cSet = setgen.__next__()
        #print(cSet)
        i = 1
        try:
            while cSet!=None:
                cSet = setgen.__next__()
                i = i + 1
        except:
            return i
        return i
