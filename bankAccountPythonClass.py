class BankAccount:
    bankName = "Citizens Bank"

    def __init__(self, name, balance, minBalance, accountNum, routingNum):
        self.customer_name = name
        self.current_balance = balance
        self.minimum_balance = minBalance
        self.__account_number = accountNum
        self.__routing_number = routingNum


    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        toBeWithdrawn = self.current_balance - amount
        if toBeWithdrawn < self.minimum_balance:
            print("""-----------------\nWithdraw failed\n-----------------\n""")
            return -1
        else:
            self.current_balance = toBeWithdrawn
            print(f"""-----------------\nWithdraw of ${amount} succeeded\n-----------------\n""")
            return 1

    def print_customer_information(self):
        print(self.bankName+"'s user:")
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("--------------\n")

    def __str__(self):
        return (f"{self.bankName} user | Name: {self.customer_name} | Balance: ${self.current_balance}/${self.minimum_balance}")