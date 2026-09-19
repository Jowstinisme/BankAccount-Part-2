from bankAccountPythonClass import BankAccount

class savingsAccount(BankAccount):
    def __init__(self, name, balance, minBalance, accountNum, routingNum, intrestRate):
        super().__init__(name, balance, minBalance, accountNum, routingNum)
        self.intrestRate = intrestRate

    def gainIntrest(self):
        intrest = self.current_balance * self.intrestRate
        self.deposit(intrest)
        print(f"Deposited ${intrest} dollars.")
