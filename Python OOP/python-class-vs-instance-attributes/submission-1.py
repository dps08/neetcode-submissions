class BankAccount:
    # Add your class attributes here
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance):
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    # @property
    # def balance(self):
    #     return self.__balance

# Don't change anything below this line
account_1 = BankAccount("Alice", 1000)
account_2 = BankAccount("Bob", 2000)


print(f"Alice's balance: ${account_1.balance}")
print(f"Bob's balance: ${account_2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")