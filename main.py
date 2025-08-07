class Account():
    account_id = 0

    def __init__(self, name, balance=0):
        Account.account_id += 1
        self.name = name
        self.__balance = balance
        self.__my_id = Account.account_id

        self.__password = input('Please set up a password: ')

        print(
            f'Welcome {self.name}, your Account ID is: {self.__my_id}. Your current balance is : ${self.__balance}')

    def check_pass(self):
        check = ''
        while check != self.__password:gh
            check = input("Please enter your password: ")
            if check != self.__password:
                print('Wrong password. Try again')

    def deposit(self, amount):
        # self.check_pass()
        self.__balance += amount
        print(f'Your new balance is ${self.__balance}')

    def withdraw(self, amount):
        self.check_pass()

        if amount > self.__balance:
            print('Your balance is low')
        else:
            self.__balance -= amount
            print(f'Your new balance is ${self.__balance}')

    def check(self):
        self.check_pass()
        print(f'Your current balance is: ${self.__balance}')


class SavingAccount(Account):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)
        print(f'''
        This is a Savings Account.
        You can withdraw your savings at the interest rate of 3% per annum
        ''')
        self.__savings = 0
        self.__time = 0
        self.i = 0

    def add_to_savings(self):
        self.check_pass()
        save = int(input('Please enter the amount you want to move into saving: '))
        if save > self.__balance:
            print('Your balance is insufficient.')
        else:
            self.__balance -= save
            self.__savings += save

    def check_savings(self):
        self.check_pass()
        print(f'Your current savings are: ${self.__savings + self.i}')

    def interest(self):
        self.i = (self.__savings * self.__time * 3 / 100)

    def inc_time(self):
        # normally this would be automated but we'll do this manually
        print("ONLY ALLOWED FOR BANK OFFICIALS")
        time = int(input("Enter the time passed (in years) since the savings account was opened: "))
        self.__time += time
        self.interest()

    def withdraw_savings(self):
        print('Withdrawing funds in savings account.')
        print(f'Withdrawn amount: ${self.__savings + self.i}')
        self.__savings = 0
        self.i -= 0

def main():
    print('''WELCOME TO JUPYTER BANKING ''')
    name = input('Please enter your name to create an account: ')

    acc1 = Account(name)

    while True:

        print(''''
        ------------------------MENU-------------------------
        1. Press to Withdraw
        2. Press to Deposit
        3. Press to Check Balance
        4. Press to EXIT
        ''')

        option = ''
        while option not in ['1', '2', '3', '4']:
            option = input()

        if option == '4':
            'Thank you for using Jupyter Banking.'
            break

        elif option == '1':
            amount = int(input("Enter an amount to withdraw: "))
            acc1.withdraw(amount)

        elif option == '2':
            amount = int(input("Enter an amount to deposit: "))
            acc1.deposit(amount)

        elif option == '3':
            acc1.check()

if __name__ == '__main__':
    main()

