class Account:
    def __init__(self,name,account_type,number):
        self.name=name
        self.account_type=account_type
        self.number=number
        self.balance=0
        #Add a new attribute to the class Account called deposits which by default is an empty list.
         #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.deposits=[]
        self.withdrawls=[]

        #Modify the withdrawal method to append each successful withdrawal to self.withdrawals

    def withdraw(self,amount):
         if amount<=0:
             return f"Withdrawal should be greater than zero"
         elif amount>self.balance:
             return f"Your balance is {self.balance},You can't withdraw {amount}"
         else:
           
           self.balance-=amount+100#to include a transaction fee of 100 per transaction.
           self.withdrawls.append(amount)
           return f"Hello {self.name}, You have withdrawn {amount}. Your new balance is {self.balance}. You paid 100 for the transaction."

    #Modify the deposit method to append each successful deposit to self.deposits
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be greater than zero"
        else:
         self.balance+=amount
         self.deposits.append(amount)
         return f"Hello {self.name}, You have deposited {amount}. Your new balance is {self.balance}"
    #Add a new method called deposits_statement which using a for loop prints each deposit in a new line

    def deposits_statement(self):
        for i in self.deposits:
            print(i,end="\n")
#Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
    def withdrawals_statement(self):
        for i in self.withdrawls:
            print(i,end="\n")

 #Add a method to show the current balance.
    def current_balance(self):
        return f"Your current balance is {self.balance}"
