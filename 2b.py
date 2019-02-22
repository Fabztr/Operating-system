import multiprocessing
import time
import random

def spawn(num):
    print("children {0} spawned".format(num))


def death(nu):
    print("child {0} has now died".format(nu))






if __name__ == "__main__":
    liste = []
    for i in range(1,20):
        p = multiprocessing.Pool(processes=spawn(i))
        liste.append(p)
        sleeping= random.randint(0,1)
        time.sleep(sleeping)
        p.close()
    for x in liste:
        x.join()