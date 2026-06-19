class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance  # Add private balance
    
    # TODO: Add getter method for balance
    @property
    def balance(self) -> int:
        return self.__balance

    # TODO: Add setter method for balance
    @balance.setter
    def balance(self, new_balance: int):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative!")



# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
# print(account.balance)
# account.set_balance(100)
# print(account.balance)
# account.set_balance(0)
# print(account.balance)
