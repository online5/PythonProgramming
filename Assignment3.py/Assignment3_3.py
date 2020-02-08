#To find the Maximum Number

def MinNo(list):
    list.sort()
   # print(list)
    return(list[0])




list=[]
No=input("Enter The Number of elements")
for i in range(No):
    Num=input("Num:")
    list.append(int(Num))

MinNumber=MinNo(list)
print("Minumum number is :",MinNumber)
