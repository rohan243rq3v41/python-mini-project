class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def get_balance(self):
        return self.balance


def main():
    accounts = {}  # Dictionary to store account_number: BankAccount pairs

    while True:
        print("\n1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            account_number = input("Enter the account number: ")
            initial_balance = float(input("Enter the initial balance: "))
            accounts[account_number] = BankAccount(account_number, initial_balance)
            print(f"Account {account_number} created.")

        elif choice == "2":
            account_number = input("Enter the account number: ")
            account = accounts.get(account_number)
            if account:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                sub_choice = input("Enter your choice (1-3): ")

                if sub_choice == "1":
                    amount = float(input("Enter the deposit amount: "))
                    account.deposit(amount)

                elif sub_choice == "2":
                    amount = float(input("Enter the withdrawal amount: "))
                    account.withdraw(amount)

                elif sub_choice == "3":
                    balance = account.get_balance()
                    print(f"Account {account_number} balance: {balance}")

                else:
                    print("Invalid choice.")

            else:
                print("Account not found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
