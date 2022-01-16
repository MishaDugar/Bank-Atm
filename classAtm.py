class ATM:
    def __init__(self,card,pin):
        self.card=card 
        self.pin=pin 
    def CashWithdrawal (self,amount):
        print("Amount Withdrawn: "+str(amount))
        newAmount=50000-amount
        print("your New balance is "+str(newAmount))
    
    def  CheckBalance (self) :
        print("Your Balance is: 50000")
            
atm= ATM(54678,3970) 
atm.CheckBalance ()
atm .CashWithdrawal(20000)