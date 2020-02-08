#4.Write a program which accept one number form user and return addition of its factors

def SumofFactors(No):
    temp=No;
    sum=0
    for i in range (1,No):
        if(temp%i==0):
            sum+=i

    return sum;

x=input("Enter The Number to calculate sum of its factors")
res=SumofFactors(x);
print("The Sum of the factors is",res)
