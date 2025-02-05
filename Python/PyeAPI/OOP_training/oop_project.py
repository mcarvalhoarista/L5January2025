from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")
Peter = BankAccount(3000, "Peter")

Dave.getBalance()
Sara.getBalance()
Peter.getBalance()

Sara.deposit(44)

Dave.withdraw(2000)
Dave.withdraw(33)

Dave.transfer(100, Peter)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)
Blaze.transfer(50, Sara)

