from checkingAccount import checkingAccount
from savingsAccount import savingsAccount

dude1Saving = savingsAccount("Brian Jacobson", 200.24, 2.00, 2172, 31872, .05)
dude2Saving = savingsAccount("Mister Saver", 5000.48, 20.00, 5872, 48927, .1)

girl1Checking = checkingAccount("Mary Suzan", 999999999.10, 0.01, 1, 2, 40000)
girl2Checking = checkingAccount("Jane Hockenberry", 50.10, 5.15, 6892, 89624, 50)

# Mary Suzan is the test subject
# Mary Suzan has opened a checking account and wants to withdraw 50000 & 20

girl1Checking.withdraw(50000)
girl1Checking.withdraw(20)

girl1Checking.print_customer_information()

# Now let's have Mary transfer Jane some money.

# Mary wants to transfer Jane $50, but accidentally puts $50000
girl1Checking.transfer(50000,girl2Checking)

# Luckily the transfer limit stopped this error. Now let's make sure no money got taken out of Mary's account. Then transfer Jane that $50.

girl1Checking.print_customer_information()

girl1Checking.transfer(50,girl2Checking)

girl1Checking.print_customer_information() # Looks like the $50 have been taken out successfully!

print("\n\nSWITCHING TO SAVINGS ACCOUNT TESTING...\n\n")

# Mister Saver has opened a checking account with $5000 as the balance with an interest rate of 10%! WOW!
# It's that time of the month where he gets some more money!
dude1Saving.print_customer_information()
dude1Saving.gainIntrest()
dude1Saving.print_customer_information() # Wow, looks like money really does print more money. He got $10 more dollars!