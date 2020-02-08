import threading
import os

def PrintAscen():
    print("Thread1 Id:",os.getpid())
    for i in range(1,51):
        print(i)

def PrintDscen():
    print("Thread2 Id:",os.getpid())
    count=50
    while(count>0):
        print(count)
        count=count-1





if __name__=="__main__":
    thread1=threading.Thread(target=PrintAscen)
    thread2=threading.Thread(target=PrintDscen)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
