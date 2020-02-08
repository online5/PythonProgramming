
def Fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact


x=input("Enter Number whose factorial to be calculated")
res=Fact(x);
print("The factorial is ",res)
