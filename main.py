class BankAccount:
    def __init__(self, account_holder, initial_balance=0, atm_pin=None):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.atm_pin = atm_pin

    def check_balance(self):
        '''
        Returns Current Balance of the User
        '''
        print(f"Current balance of {self.account_holder} is: {self.balance}")

    def validate_pin(self):
        '''
        Validates the user input pin with registered pin.
        '''
        entered_pin = int(input("Enter your Transaction PIN: "))
        return entered_pin == self.atm_pin

    def deposit(self, amount):
        '''
        deposits amount greater than 0 and checks if amout are in multiples of 100 or not.
        '''
        if amount > 0 and amount % 100 == 0:
            self.balance += amount
            print(f"Deposited {amount} Rs.\nNew balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero and in multiples of 100.")

    def withdraw(self, amount):
        '''
        for withdrawing, if amount greater than 10000 6% intrest is charged
        '''
        if self.atm_pin is None:
            print("Transaction PIN is not set. Please set your Transaction PIN.")
            return
        if 0 < amount <= self.balance:    #If amount is greater than zero or equal to account balance
            if amount <= 10000 and self.validate_pin(): 
                self.balance -= amount
                print(f"Withdrew {amount} Rs.\nNew balance: {self.balance}")
            elif amount > 10000: #If Amount is greater than 10,000
                if self.validate_pin():
                    charge = amount * 0.06
                    total_withdraw = amount + charge
                    if total_withdraw <= self.balance:
                        self.balance -= total_withdraw
                        print(f"Withdrew {amount} Rs with charges of {charge} Rs.\nNew balance: {self.balance}")
                    else:
                        print("Insufficient balance to cover withdrawal and charges.")
                else:
                    print("Invalid PIN.")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self):
        '''
        For Changing pin
        '''
        if self.validate_pin():
            new_pin = int(input("Enter new PIN: "))
            self.atm_pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN.")

    def loan_transfer(self, amount):
        '''
        for taking loan
        '''
        if amount > 0:
            self.balance += amount
            print(f"Loan of {amount} Rs transferred.\nNew balance: {self.balance}")
        else:
            print("Loan amount must be greater than zero.")

def main():
    print("Welcome to Our Banking Service!")
    try:
        account_holder = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: "))
        atm_pin = int(input("Set your Transaction PIN: "))
        user_account = BankAccount(account_holder, initial_balance, atm_pin)
        
        while True:
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Loan Transfer")
            print("6. Exit")
            choice = input("Enter option number: ")
            
            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    user_account.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    user_account.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "3":
                user_account.check_balance()
            elif choice == "4":
                user_account.change_pin()
            elif choice == "5":
                try:
                    amount = float(input("Enter loan transfer amount: "))
                    user_account.loan_transfer(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "6":
                print("Thank you for using our banking services!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter valid account information.")

if __name__ == "__main__":
    main()