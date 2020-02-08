
def NumberPattern(No):
    while(No>0):
        for i in range(1,No+1):
            print("* ") ,
        No=No-1;
        print("")




x=input("Enter The Number of rows to printed")
NumberPattern(x)
