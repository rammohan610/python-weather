from bank_accounts import *

Ram = BankAccount(1000, "Ram")
Dave = BankAccount(2000, "Dave")

Ram.getBalance()
Dave.getBalance()

Ram.deposit(500)
Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000,Ram)
Dave.transfer(100,Ram)

Ganga = InterestRewardsAcct(1000,"Ganga")

Ganga.getBalance()
Ganga.deposit(100)
Ganga.transfer(100,Ram)

Dhyana = SavingsAcct(1000,"Dhyana")
Dhyana.getBalance()
Dhyana.deposit(100)
Dhyana.transfer(1000, Dave)
