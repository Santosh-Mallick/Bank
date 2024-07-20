# BankAccount Class

This is a simple implementation of a `BankAccount` class in Python. The class supports basic banking operations such as depositing, withdrawing, checking balance, changing PIN, and loan transfer. It includes features such as ATM PIN validation and interest charges for large withdrawals.

## Features

- **Deposit**: Add funds to the account, ensuring the amount is greater than zero and in multiples of 100.
- **Withdraw**: Withdraw funds from the account. If the withdrawal amount exceeds 10,000, a 6% interest charge is applied.
- **Check Balance**: View the current balance of the account.
- **Change PIN**: Change the transaction PIN after validating the current one.
- **Loan Transfer**: Transfer a loan amount to the account.
