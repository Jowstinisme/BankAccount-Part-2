from bankAccountPythonClass import BankAccount

class checkingAccount(BankAccount):
    def __init__(self, name, balance, minBalance, accountNum, routingNum, transferLimit):
        super().__init__(name, balance, minBalance, accountNum, routingNum)
        self.transferLimit = transferLimit