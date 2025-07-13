class BankAccount:
    def __init__(self , account_number , balance):
        self.account_number = account_number
        self.__balance = balance # this variable is privete here now (__balance )

    def deposite(self , amount):
        self.__balance += amount
        print(f'Deposited {amount}.New Amount {self.__balance}')
    
    def get_balance(self):
        return self.__balance # comtrolled access 
    

account = BankAccount('123456' , 5000)

account.deposite(2000)
print(account.get_balance())


print(account.__balance)
"""
print(account.__balance)
          ^^^^^^^^^^^^^^^^^
AttributeError: 'BankAccount' object has no attribute '__balance'. 
Did you mean: 'get_balance'?
"""