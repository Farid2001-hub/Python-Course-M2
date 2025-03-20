import logging

# Configurer le logging
logging.basicConfig(filename='bank.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            logging.error(f"Invalid deposit amount: {amount}")
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        logging.info(f"Deposit: ${amount} | New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            logging.error(f"Invalid withdrawal amount: {amount}")
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            logging.warning(f"Insufficient funds for withdrawal: ${amount}")
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        logging.info(f"Withdrawal: ${amount} | New Balance: ${self.balance}")

    def get_balance(self):
        return self.balance
