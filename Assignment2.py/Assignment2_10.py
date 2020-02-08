def SumofDigits(No):
    sum=0
    temp=No;
    while(temp>0):
        rem=temp%10;
        temp=temp/10;
        sum+=rem;
    return sum




No=input("Enter The Number whose SumofDigits is to be calculated")
res=SumofDigits(No)
print("The SumofDigits is ",res)
