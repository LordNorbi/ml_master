
from taskset import TaskSet
from task import Task
from blocks import *
from tasksets.setgenerator import SetGenerator

def main():
    
    generator = SetGenerator()
    set2 = generator.size2()
    print("set2 created")
    setgen2 = set2.variants()
    print("Contains "+str(generator.getPossibilities(set2))+" Sets")
    
    set3 = generator.size3()
    print("set3 created")
    setgen3 = set3.variants()
    print("Contains "+str(generator.getPossibilities(set3))+" Sets")
    
    set4 = generator.size4()
    print("set4 created")
    setgen4 = set4.variants()
    print("Contains "+str(generator.getPossibilities(set4))+" Sets")
    
    set5 = generator.size5()
    print("set5 created")
    setgen5 = set5.variants()
    print("Contains "+str(generator.getPossibilities(set5))+" Sets")
    
    set6 = generator.size6()
    print("set6 created")
    setgen6 = set6.variants()
    print("Contains "+str(generator.getPossibilities(set6))+" Sets")

#cSet = set2gen.__next__()
#print(cSet)
#   i=1
#try:
#   while i<1000000:
#       cSet = set2gen.__next__()
#       i =i+ 1
#except:
#    print(i)
#print(i)
#print("bla")
#print(cSet)


if __name__ == "__main__":
    main()

