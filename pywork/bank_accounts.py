class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw Interupted : {error}")

    def transfer(self,amount,account):
        try:
            print("\n***********\n\nBeginning Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"Transfer Incomplete.  ❌ {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete with rewards")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete with rewards")
        self.getBalance()

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance = self.balance - amount - self.fee
            print("\nWithdraw Complete with fees.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw Interupted : {error}")