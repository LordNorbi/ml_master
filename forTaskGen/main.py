import sys
sys.path.append('../')

import argparse
import logging, coloredlogs

# inspect
import inspect
import pkgutil
import importlib


from distributor import Distributor
from taskgen.setgenerator import SetGenerator
from monitors.loggingMonitor import LoggingMonitor

def main():
    
    dis = Distributor()
    print("distributor created")
    
    gen = SetGenerator()
    set2 = gen.size2()
    print("set2 created")
    
    logmon = LoggingMonitor()
    print("monitor created")
    
    dis.add_job(set2,logmon)
    print("finished")






if __name__ == "__main__":
    main()



