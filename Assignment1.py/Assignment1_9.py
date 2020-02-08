

#To print 10 even Number



def PrintEven(x):

       if(x==0):
           return

       for i in range(2,(2*x+1)):
           if(i%2==0):
               print(i),




x=input("Enter How many Even number you want to print");
PrintEven(x);
