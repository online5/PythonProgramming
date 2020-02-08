def StarPrinting(x):
    if(x==0):
        return;

    while(x>0):
        print("*") ,
        x=x-1


x=input("Enter how many times you want to print * ")
StarPrinting(x);
