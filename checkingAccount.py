from bankAccountPythonClass import BankAccount

class checkingAccount(BankAccount):
    def __init__(self, name, balance, minBalance, accountNum, routingNum, transferLimit):
        super().__init__(name, balance, minBalance, accountNum, routingNum)
        self.transferLimit = transferLimit

    def withdraw(self, amount):
        if amount > self.transferLimit:
            print(f"Withdraw of ${amount} failed, unable to withdraw more than ${self.transferLimit}.")
            return -1
        else:
            return super().withdraw(amount)

    def transfer(self, amount, otherAccount):
        if self.withdraw(amount) != -1:
            # otherAccount should be another bank account function
            otherAccount.deposit(amount)
        else:
            print(f"Transfer failed, ${amount} is larger than transfer limit of ${self.transferLimit}.")