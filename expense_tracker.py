import csv

# List to store expenses
expenses = []

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (Food, Travel, etc.): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    
    expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
    expenses.append(expense)
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    print("Date       | Category | Amount | Description")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
    print()

# Function to set and track the budget
def track_budget():
    budget = float(input("Enter your monthly budget: "))
    total_expense = sum(exp['amount'] for exp in expenses)
    
    print(f"Total expenses so far: {total_expense}")
    if total_expense > budget:
        print("Warning: You have exceeded your budget!\n")
    else:
        print(f"You have {budget - total_expense} left for the month.\n")

# Function to save expenses to a file
def save_expenses():
    with open(r"E:\\self\\akash_test\\simpliLearn\\Python\\expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for exp in expenses:
            writer.writerow([exp['date'], exp['category'], exp['amount'], exp['description']])
    print("Expenses saved successfully!\n")

# Function to load expenses from a file
def load_expenses():
    global expenses
    try:
        with open(r"E:\\self\\akash_test\\simpliLearn\\Python\\expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            for exp in expenses:
                exp['amount'] = float(exp['amount']) 
        print("Expenses loaded successfully!\n")
    except FileNotFoundError:
        print("No previous expense records found.\n")

# Function to display the menu and handle user choices
def menu():
    load_expenses()
    while True:
        print("Personal Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


menu()
