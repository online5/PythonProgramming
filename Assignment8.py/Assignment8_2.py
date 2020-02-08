
import threading

def Factors(Number):
        No=Number
        list=[]
        count=0
        while(No%2==0):
           print(2),
           list.append(2)
           No=No/2

        for i in range(2,No):
            if(No%i==0):
                No=No/i
                print(i),
                list.append(i)

        if(No>2):
            print(No),
            list.append(No)

        return list

def EvenFactor(Number):
    list=[];
    sum=0
    no=0
    list=Factors(Number);
    print("")
    for i in range(len(list)):
        no=list[i]
        if(no%2==0):
            sum=sum+no;
    print("The sum is :",sum)


def OddFactor(Number):
    list=[];
    sum=0
    no=0
    list=Factors(Number);
    print("")
    for i in range(len(list)):
        no=list[i]
        if(no%2==1):
            sum=sum+no;
    print("The sum is :",sum)


if __name__ == '__main__':
    Even=threading.Thread(target=EvenFactor,args=(20,))
    Odd=threading.Thread(target=OddFactor,args=(25,))


    Even.start()
    Odd.start()

    Even.join()
    Odd.joim()
    
