import threading
import os


def UpperCount(String):
    count=0
    for i in range(len(String)):
        if(String[i].isupper()):
            #print(String[i])
            count=count+1
    print("UpperCount:",count)
    print("Upperthread",os.getpid())

def LowerCount(String):
    count=0
    for i in range(len(String)):
        if(String[i].islower()):
            #print(String[i])
            count=count+1
    print("LowerCase :",count)
    print("Lowerthread",os.getpid())

def DigitCount(String):
    count=0
    for i in range(len(String)):
        if(String[i].isdigit()):
            #print(String[i])
            count=count+1
    print("Digits:",count)
    print("Digitthread",os.getpid())


#print("The UpperCase are :",UpperCount("Dee45Pak7"))
#print("The LowerCase are :",LowerCount("Dee45Pak7"))
#print("The Digits are :",DigitCount("Dee45Pak76"))


x=raw_input("Enter String:")

if __name__=="__main__":
    Upper=threading.Thread(target=UpperCount,args=(x,))
    Lower=threading.Thread(target=LowerCount,args=(x,))
    Digit=threading.Thread(target=DigitCount,args=(x,))
    print("The Main Thread id is :",os.getpid())




    Upper.start()
    Lower.start()
    Digit.start()

    Upper.join()
    Lower.join()
    Digit.join()
