from expenses import Expense
from typing import List
import datetime
import calendar

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 17000
    
# Get user input for expense.
    expense = get_user_expense()
   
# Write their expense to a file
    save_expense_to_file(expense, expense_file_path)
    
# Read file and summarize expense
    summarize_expense(expense_file_path, budget)
    

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))  
    expense_categories = [
        "🍲 Groceries",
        "💰 Bills",
        "🏡 House",
        "🌍 Travel",
        "🎁 Fun",
        "🧭 Other",
    ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1  
        
        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again.")
       

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print(f"Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:        
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category,
            )
            print(line_expense)
            expenses.append(line_expense)
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses By Category :")        
    for key, amount in amount_by_category.items():
        print(green(f"  {key}: Ksh.{amount:.2f}"))

    total_spent = sum(ex.amount for ex in expenses)
    print(blue(f"🤑 Total Spent: Ksh.{total_spent:.2f} this month!"))
    
    remaining_budget = budget - total_spent
    print(purple(f"✅ Remaining budget is: Ksh.{remaining_budget:.2f}"))
    if remaining_budget < 0:
        print(red("🤔 You've exceeded your budget!"))

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
   
    daily_budget = remaining_budget / remaining_days
    print(orange(f"🏦 Daily budget: Ksh.{daily_budget:.2f}"))

def orange(text):
    return f"\033[33m{text}\033[0m"
def blue(text):
    return f"\033[34m{text}\033[0m"
def green(text):
    return f"\033[32m{text}\033[0m"
def red(text):
    return f"\033[31m{text}\033[0m"
def purple(text):
    return f"\033[35m{text}\033[0m"

if __name__ == "__main__":
    main()