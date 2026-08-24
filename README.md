 Banking Application Using OOP

A Python-based banking application that demonstrates important object-oriented programming concepts such as abstraction, inheritance, encapsulation, polymorphism, operator overloading, exception handling, and object serialization.

## Features

- Abstract Account base class.
- SavingsAccount and CheckingAccount subclasses.
- Deposit and withdrawal operations.
- Savings account balance validation.
- Checking account overdraft facility.
- Private account attributes using encapsulation.
- Operator overloading using the + operator.
- Saving multiple account objects to a file.
- Loading saved accounts using Python's pickle module.
- Exception handling for invalid transactions and file errors.

The abc module is used to create abstract base classes and require subclasses to implement abstract methods. [web:2]

## Technologies Used

- Python 3
- Object-Oriented Programming
- Abstract Base Classes
- Inheritance
- Encapsulation
- Polymorphism
- Operator Overloading
- Exception Handling
- File Handling
- Object Serialization

## Requirements

- Python 3.8 or later
- No external packages are required

The program uses Python's built-in modules:

python
from abc import ABC, abstractmethod
import pickle


## Project Structure

text
banking-application/
│
├── banking_application.py
├── accounts.pkl
└── README.md


## How to Run

### 1. Save the Python Program

Save the provided code in a file named:

text
banking_application.py


### 2. Open the Terminal

Open a terminal or command prompt and navigate to the folder containing the Python file.

### 3. Run the Program

On Windows:

bash
python banking_application.py


On Linux or macOS:

bash
python3 banking_application.py


After execution, the program creates a file named:

text
accounts.pkl


This file stores the savings and checking account objects.

## Classes and Methods

### Account Class

Account is an abstract base class.

It contains the common properties and methods shared by all account types.

python
class Account(ABC):


#### Main Features

- Stores the account number.
- Stores the account balance.
- Provides read-only properties for account number and balance.
- Provides an internal method to update the balance.
- Defines abstract deposit() and withdraw() methods.
- Overloads the + operator.

The Account class cannot be directly instantiated because it contains abstract methods.

### SavingsAccount Class

SavingsAccount inherits from the Account class.

python
class SavingsAccount(Account):


It includes:

- Account number.
- Account balance.
- Interest rate.
- Deposit validation.
- Withdrawal validation.

A savings account cannot withdraw more money than its available balance.

### CheckingAccount Class

CheckingAccount also inherits from the Account class.

python
class CheckingAccount(Account):


It includes:

- Account number.
- Account balance.
- Overdraft limit.
- Deposit validation.
- Withdrawal validation.

A checking account can withdraw more than its current balance, provided that the overdraft limit is not exceeded.

## Account Transactions

### Savings Account Transactions

The savings account is created with:

python
savings = SavingsAccount("S101", 10000, 4.5)


Initial balance:

text
₹10000


After depositing ₹2000:

text
₹10000 + ₹2000 = ₹12000


After withdrawing ₹3000:

text
₹12000 - ₹3000 = ₹9000


Final savings account balance:

text
₹9000


### Checking Account Transactions

The checking account is created with:

python
checking = CheckingAccount("C101", 5000, 2000)


Initial balance:

text
₹5000


The program withdraws ₹6000.

The maximum permitted withdrawal is:

text
Current balance + overdraft limit
₹5000 + ₹2000 = ₹7000


Since ₹6000 is within the permitted limit, the withdrawal is successful.

Final checking account balance:

text
₹5000 - ₹6000 = -₹1000


## Operator Overloading

The __add__() metho…
