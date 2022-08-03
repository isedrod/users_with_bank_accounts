class BankAccount:

    bank_name = "First Bank of the Wild West"
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0, balance=0):
        self.interest = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

        # your code here
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        print(f"Your current balance is : ${self.balance}")
        return(self)
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance += round(self.balance * self.interest)
        else:
            print("No balance to gain interest")
        return self
        # your code here

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def display_user_balance(self):
        print('Balance: ', self.account.balance)
        return self

    def transfer_money(self, other, amount):
        self.account.balance -= amount
        other.account.balance += amount
        return self




user_1 = User("Isaac", "isaac@email.com")
user_2 = User("Phillis", "phil@email.com")
user_3 = User("Willis", "will@email.com")
user_1.transfer_money(user_3, 400)
user_1.display_user_balance()
user_3.display_user_balance()

user_1.account.deposit(100).deposit(100).deposit(100).display_account_info()

user_2.account.deposit(100).deposit(100).withdraw(100).display_account_info()
user_3.account.deposit(100).deposit(50000).withdraw(800).display_account_info()

    # def make_deposit(self, amount):
    # # we can call the BankAccount instance's methods
    #     self.account.balance += amount
    # # or access its attributes
    #     print(self.account.balance)
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account.balance -= amount
    #     return self

    # def display_account_info(self):
    #     print(f"Balance: ${self.balance} Interest Rate: {self.int_rate}")
    #     return self