import json
import os
from datetime import datetime
class FinanceTracker:
    def __init__(self):
        self.transactions = []
        if os.path.exists('transactions.json'):
            with open('transactions.json', 'r') as file:
                self.transactions = json.load(file)
    def save_data(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file, indent=4)
    def add_income(self):
        amount=float(input("Enter income amount: "))
        self.transactions.append({
            'type': 'income',  
            'amount': amount,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'category': 'income'
        })
        self.save_data()
        print("Income added successfully.")
    def add_expense(self):
        amount=float(input("Enter expense amount: "))
        category=input("Enter expense category: ")
        self.transactions.append({
            'type': 'expense',  
            'amount': amount,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        self.save_data()
        print("Expense added successfully.")
    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        print("=======Transactions========")
        for transaction in self.transactions:
            print(f"Date : {transaction['date']}|"
                f"Type : {transaction['type'].capitalize()}|"
                f"Amount : {transaction['amount']}|"
                f"Category: {transaction['category']}")
    def total_balance(self):
        income = 0
        expense = 0
        for transaction in self.transactions:
            if transaction['type'] == 'income':
                income += transaction['amount']
            else:
                expense += transaction['amount']
        balance = income - expense
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Total Balance: {balance}")
    def category_report(self):
        category_totals = {}
        if not self.transactions:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            category = transaction['category']
            amount = transaction['amount']
            if category  in category_totals:
                category_totals[category]+= amount
            else:
                category_totals[category] = amount
            
        print("=======Category Summary========")
        for category, total in category_totals.items():
            print(f"Category: {category} | Total: {total}")
tracker = FinanceTracker()
while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Total Balance")
    print("5. Category Report")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        tracker.add_income()
    elif choice == '2':
        tracker.add_expense()
    elif choice == '3':
        tracker.view_transactions()
    elif choice == '4':
        tracker.total_balance()
    elif choice == '5':
        tracker.category_report()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
