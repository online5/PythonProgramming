




def SumOfElements(list):
    sum=0
    x=len(list)
    for i in range(x):
       sum=sum+list[i]
    return sum


list=[]
No=input("Enter the number of inputs")
for i in range(No):
    num=input("Num:")
    list.append(int(num))

res=SumOfElements(list)


print("The Sum is :",res)
