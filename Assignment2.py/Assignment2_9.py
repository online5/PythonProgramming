def NoofDigits(No):
    count=0;
    temp=No
    if(No==0):
        return 0;
    while(temp>0):
        count=count+1
        temp/=10
    return count



x=input("Enter The Number for which digits is to be calculated ")
ans=NoofDigits(x)
print("The number of digits are ",ans)
