from expense import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    #Get user to input expense.
    expense = get_user_expense()

    # Write their expense to file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


    

def get_user_expense():
    print(f"Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["Food", "Home", "Work", "Fun", "Other", ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")
        

        value_index = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_index}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)
            return new_expense
        else:
            print("Invalid category, please try again!")
    

    

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")



def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing User Expense!")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(name = expense_name, amount = float(expense_amount), category = expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category:")    
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You have spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining ${remaining_budget:.2f} this month!")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    print(f"Remaining days in the current month, {remaining_days}")

if __name__ == "__main__":
    main()