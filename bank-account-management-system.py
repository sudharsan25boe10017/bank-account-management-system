from abc import ABC, abstractmethod
import pickle


# Abstract Base Class
class Account(ABC):

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    # Getter for account number
    @property
    def account_number(self):
        return self.__account_number

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Internal method to change balance
    def _set_balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Operator overloading
    def __add__(self, other):
        if isinstance(other, Account):
            return self.balance + other.balance
        raise TypeError("Can only add two Account objects")


# Savings Account
class SavingsAccount(Account):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be numeric")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be numeric")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds in Savings Account")

        self._set_balance(self.balance - amount)


# Checking Account
class CheckingAccount(Account):

    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be numeric")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be numeric")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        # Checking account can use overdraft
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")

        self._set_balance(self.balance - amount)


# Save account objects using pickle
def save_accounts(accounts, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(accounts, file)

        print("Accounts saved successfully.")

    except Exception as e:
        print("Error while saving:", e)

    finally:
        print("Save operation completed.")


# Load account objects using pickle
def load_accounts(filename):
    try:
        with open(filename, "rb") as file:
            accounts = pickle.load(file)

        print("Accounts loaded successfully.")
        return accounts

    except FileNotFoundError:
        print("Save file not found.")
        return []

    except (pickle.UnpicklingError, EOFError):
        print("Corrupted save file.")
        return []

    except Exception as e:
        print("Error while loading:", e)
        return []

    finally:
        print("Load operation completed.")


# Main Program
try:

    # Creating objects
    savings = SavingsAccount("S101", 10000, 4.5)
    checking = CheckingAccount("C101", 5000, 2000)

    print("Savings Account Balance:", savings.balance)
    print("Checking Account Balance:", checking.balance)

    # Deposit
    savings.deposit(2000)
    print("Savings balance after deposit:", savings.balance)

    # Withdrawal
    savings.withdraw(3000)
    print("Savings balance after withdrawal:", savings.balance)

    # Checking withdrawal using overdraft
    checking.withdraw(6000)
    print("Checking balance after overdraft:", checking.balance)

    # Operator overloading
    total_balance = savings + checking
    print("Combined balance:", total_balance)

    # Save accounts
    accounts = [savings, checking]
    save_accounts(accounts, "accounts.pkl")

    # Load accounts
    loaded_accounts = load_accounts("accounts.pkl")

    for account in loaded_accounts:
        print(
            "Account Number:",
            account.account_number,
            "| Balance:",
            account.balance
        )

except (TypeError, ValueError) as e:
    print("Transaction Error:", e)

finally:
    print("Banking application completed.")
