class BankAccount:
    def __init__(self, account_num, bal=0):
        self.account_num = account_num
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print(f"Deposit {amt}. New balance is {self.bal}.")

    def withdraw(self, amt):
        if amt > self.bal or amt < 0:
            print("Insufficient funds.")
        else:
            self.bal -= amt
            print(f"Withdraw {amt}. New balance is {self.bal}.")

    def get_balance(self):
        print(f"Balance for account {self.account_num} is {self.bal}.")

class SavingsAccount(BankAccount):
    def __init__(self, account_num, bal=0, interest_rate=0.03):
        super().__init__(account_num, bal)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.bal * self.interest_rate
        self.bal += interest
        print(f"Added {interest} in interest. New balance is {self.bal}.")

def main():
    account_num = input("Enter account number : ")
    account_type = input("Enter account type [b=BankAccount, s=SavingsAccount] : ")

    if account_type == 'b':
        account = BankAccount(account_num)
    elif account_type == 's':
        account = SavingsAccount(account_num)
    else:
        print("Invalid account type.")
        return

    while True:
        print("\n---Menu---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get balance")

        if account_type == 's':
            print("4. Add interest")

        print("0. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == 2:
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == 3:
            account.get_balance()
        elif choice == 4 and account_type == 's':
            account.add_interest()
        elif choice == 0:
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()