#class Bank

class Bank:
    ROI=10.5

    def __init__(self,Value1,Value2):
        self.Name=Value1
        self.Amount=Value2


    def Deposit():
        Amt=input("Enter The Amount to be Deposited")
        self.Amount=self.Amount+Amt

    def Withdraw():
        if(self.Amount<0):
            print("Insufficient Balance")
            return
        amt=input("ENter The amount to debit")
        self.Amount=self.Amount-amt


    def CalculateInterest():
        Inter=self.Amount*Bank.ROI
             
