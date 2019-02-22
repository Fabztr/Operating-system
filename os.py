import time
import random
import run
import multiprocessing

class task:
    def __init__(self, children):
        self._children = children
        print("Children {0} will now launch".format(self._children))
    
    
    def __del__(self):
        print("children {0} - has died".format(self._children))
    
    
    def phoenix():
        print("all children has died, process will start over")
    
    
    def runtime(self):
        
        sleeping = random.randint(1,30)
        
        print("Children {0} will now sleep for {1} seconds").format(self._children, sleeping)
        time.sleep(sleeping)
        print("Child {0} - End".format(self._children))




def mainprogram():
    poolOfChildren = []
    end_time = time.time() + 1 * 10
    while time.time() < end_time:
        for child in range(1,5):
            childs = "Parent: creating child {0}".format(child)
            print(childs)
            poolOfChildren.append(multiprocessing.Process(name = childs, target = task(child).runtime))
    
        print("Parent will now launch all the children:")
        for process in poolOfChildren:
            process.start()
    
        while poolOfChildren:
            for pross in poolOfChildren:
                if not pross.is_alive():
                    pross.join()
                    poolOfChildren.remove(pross)
                    del(pross)
                
            