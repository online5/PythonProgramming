# To check if a number is prime or not


def PrimeCheck(No):
    temp=No
    if(No<=1):
        return False
    elif(No==2|No==3):
        return True

    for i in range(2,No+1):
        if(No%i==0):
            return False


    return True


x=input("Enter The number to be test primility")
if(PrimeCheck(x)):
    print("The Number is prime")
else:
    print("Not A prime Number")
