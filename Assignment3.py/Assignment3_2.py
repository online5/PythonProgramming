#To find the Maximum Number

def MaxNo(list):
    list.sort()
   # print(list)
    return(list[-1])




list=[]
No=input("Enter The Number of elements")
for i in range(No):
    Num=input("Num:")
    list.append(int(Num))

MaxNumber=MaxNo(list)
print("Maximum number is :",MaxNumber)
