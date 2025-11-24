"""
Simple Expense Tracker
A beginner-friendly program to track your daily expenses
"""

import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.data_file = "expenses_data.json"
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return []
        except:
            return []
    
    def save_expenses(self):
        """Save expenses to file"""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.expenses, file, indent=2)
            return True
        except:
            return False
    
    def add_expense(self):
        """Add a new expense"""
        print("\nADD NEW EXPENSE")
        print("---------------")
        
        try:
            amount = float(input("Enter amount spent: "))
            category = input("Enter category (food, transport, shopping, etc): ").strip()
            description = input("Enter description: ").strip()
            
            if not category:
                category = "other"
            if not description:
                description = "no description"
            
            expense = {
                'amount': amount,
                'category': category,
                'description': description,
                'date': datetime.now().strftime("%Y-%m-%d")
            }
            
            self.expenses.append(expense)
            self.save_expenses()
            print(f"Success! Added ${amount} to {category}")
            
        except ValueError:
            print("Error: Please enter a valid number for amount")
    
    def view_all_expenses(self):
        """View all expenses"""
        print("\nALL EXPENSES")
        print("------------")
        
        if not self.expenses:
            print("No expenses recorded yet!")
            return
        
        total = 0
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. ${expense['amount']} - {expense['category']} - {expense['description']} - {expense['date']}")
            total += expense['amount']
        
        print(f"\nTOTAL SPENT: ${total:.2f}")
    
    def view_summary(self):
        """View spending summary by category"""
        print("\nSPENDING SUMMARY")
        print("----------------")
        
        if not self.expenses:
            print("No expenses recorded yet!")
            return
        
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']
        
        total = 0
        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")
            total += amount
        
        print(f"\nTOTAL: ${total:.2f}")
    
    def delete_expense(self):
        """Delete an expense"""
        if not self.expenses:
            print("No expenses to delete!")
            return
        
        print("\nDELETE EXPENSE")
        print("--------------")
        
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. ${expense['amount']} - {expense['category']} - {expense['description']}")
        
        try:
            choice = int(input(f"Enter expense number to delete (1-{len(self.expenses)}): "))
            if 1 <= choice <= len(self.expenses):
                deleted_expense = self.expenses.pop(choice-1)
                self.save_expenses()
                print(f"Deleted expense: ${deleted_expense['amount']} - {deleted_expense['category']}")
            else:
                print("Invalid expense number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main program function"""
    print("=" * 40)
    print("PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    
    tracker = ExpenseTracker()
    
    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_all_expenses()
        elif choice == '3':
            tracker.view_summary()
        elif choice == '4':
            tracker.delete_expense()
        elif choice == '5':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please enter 1-5")

if __name__ == "__main__":
    main()