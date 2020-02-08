
def NumberPattern(No):

    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j) ,
        print(" ")

x=input("Enter the number of rows")
NumberPattern(x)
