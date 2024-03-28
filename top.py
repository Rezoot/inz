import cv2
import onebyone
import onebyone2
import diffphoto
import vibe
from time import sleep
from multiprocessing import Process
 
# a custom function that blocks for a moment
def org():
    onebyone.org()


def task1():
    onebyone.obraz()

def task2():
    onebyone2.obraz()

def task3():
    diffphoto.obraz()

def task4():
    vibe.obraz()
 
def task5():
    vibe.obrazmaly()

def task6():
    vibe.obrazmini()



if __name__ == '__main__':
    
    # create a process
    one = Process(target=task1)
    one2 = Process(target=task2)
    back = Process(target=task3)
    vibe = Process(target=task4)
    vibemale = Process(target=task5)
    vibemini = Process(target=task6)

    orginalne = Process(target=org)
    
    

    #orginalne.start()
    #one.start()
    #one2.start()
    #back.start()
    #vibe.start()
    #vibemale.start()
    #vibemini.start()
    # wait for the process to finish
    print('Waiting for the process...')
    