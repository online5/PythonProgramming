class Arthematic:
    def SumofFactors(self):
        val=self.Value
        list=self.Factors()
        print("The Sum of the Elements in THe list is ",sum(list))

    def __init__(self,Val):
        self.Value=Val
    def chkPrime(self):
        val=self.Value
        if(val<=1):
            return False
        elif(val==2):
            return True
        else:
            for i in range(2,val):
                if(val%i==0):
                    return False;
        return True

    def Factors(self):

        No=self.Value
        list=[]
        count=0
        while(No%2==0):
           print(2),
           list.append(2)
           No=No/2

        for i in range(2,No):
            if(No%i==0):
                No=No/i
                print(i),
                list.append(i)

        if(No>2):
            print(No),
            list.append(No)

        return list



if(__name__=="__main__"):

    Value=input("Enter Value to be operated")
    obj1=Arthematic(Value)
    list=[]
    list=obj1.Factors()
    print("The List is:",list)
    obj1.SumofFactors()
