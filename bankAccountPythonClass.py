class BankAccount:
    bankName = "Citizens Bank"

    def __init__(self, name, balance, minBalance):
        self.customer_name = name
        self.current_balance = balance
        self.minimum_balance = minBalance


    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        toBeWithdrawn = self.current_balance - amount
        if toBeWithdrawn < self.minimum_balance:
            print("""-----------------\nWithdraw failed\n-----------------\n""")
            return -1
        else:
            self.current_balance = toBeWithdrawn
            return 1

    def print_customer_information(self):
        print(self.bankName+"'s user:")
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("--------------\n")

    def __str__(self):
        return (f"{self.bankName} user | Name: {self.customer_name} | Balance: ${self.current_balance}/${self.minimum_balance}")

dude1 = BankAccount("John Doe", 2000, 100)
dude2 = BankAccount("Friend Guy",1000000000,5)

print(dude1.print_customer_information())
dude1.withdraw(2000)
dude1.withdraw(100)
print(dude1.print_customer_information())

print(dude1)