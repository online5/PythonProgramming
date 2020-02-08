import threading


def EvenList(list):
    no=0
    for i in range(len(list)):
        no=list[i]
        if(no%2==0):
            print(no),

def OddList(list):
    no=0
    for i in range(len(list)):
        no=list[i]
        if(no%2==1):
            print(no),

number=input("Enter the number of elements in list")
list=[]

for i in range(number):
    x=input("Enter ListItem :")
    list.append(x)



if __name__=="__main__":


    thread1=threading.Thread(target=EvenList,args=(list,))
    thread2=threading.Thread(target=OddList,args=(list,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
