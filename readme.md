# BankAccount

This is a simple implementation of a `BankAccount` class in Python. The class supports basic banking operations such as depositing, withdrawing, checking balance, changing PIN, and loan transfer. It includes features such as ATM PIN validation and interest charges for large withdrawals.

## Features

- **Deposit**: Add funds to the account, ensuring the amount is greater than zero and in multiples of 100.
- **Withdraw**: Withdraw funds from the account. If the withdrawal amount exceeds 10,000, a 6% interest charge is applied.
- **Check Balance**: View the current balance of the account.
- **Change PIN**: Change the transaction PIN after validating the current one.
- **Loan Transfer**: Transfer a loan amount to the account.

## Working Example

```bash
Welcome to Our Banking Service!
Enter account holder's name: santosh mallick
Enter initial balance: 3000
Set your Transaction PIN: 4321

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 4
Enter your Transaction PIN: 4321
Enter new PIN: 1234
PIN changed successfully.

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 1
Enter deposit amount: 2000
Deposited 2000.0 Rs.
New balance: 5000.0

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 2
Enter withdrawal amount: 1000
Enter your Transaction PIN: 1234
Withdrew 1000.0 Rs.
New balance: 4000.0

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 3
Current balance of santosh mallick is: 4000.0

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 5
Enter loan transfer amount: 1000
Loan of 1000.0 Rs transferred.
New balance: 5000.0

Select an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Change PIN
5. Loan Transfer
6. Exit
Enter option number: 6
Thank you for using our banking services!
