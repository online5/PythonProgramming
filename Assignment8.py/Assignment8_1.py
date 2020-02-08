import threading


def EvenNo():
    count=10
    number=1;
    while(count>0):

        if(number%2==0):
            print(number)
            count=count-1
        number=number+1


def OddNo():
    count=10;
    number=1
    while(count>0):

        if(number%2==1):
            print(number)
            count=count-1
        number=number+1

if __name__=="__main__":

    Even=threading.Thread(target=EvenNo)
    Odd=threading.Thread(target=OddNo)

    Even.start();
    Odd.start();
