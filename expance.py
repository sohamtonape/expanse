class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        expense = {'description': description, 'amount': amount}
        self.expenses.append(expense)
        print(f"Expense added: {description} - ${amount}")

    def view_expenses(self):
        total_expense = sum(expense['amount'] for expense in self.expenses)
        print("Expenses:")
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']}")
        print(f"Total Expense: ${total_expense}")

    def remove_expense(self, description):
        original_length = len(self.expenses)
        self.expenses = [expense for expense in self.expenses if expense['description'].lower() != description.lower()]
        if len(self.expenses) < original_length:
            print(f"Expense removed: {description}")
        else:
            print(f"No expense found with the description: {description}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Remove an expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ").strip()
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(description, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            description = input("Enter expense description to remove: ").strip()
            tracker.remove_expense(description)
        elif choice == "4":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
