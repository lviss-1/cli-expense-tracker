'''
This is going to be an expense tracker used in the CLI to re-build my coding skills 

Basic functionality:
1) Add expense - Each expense has an id, date, amount, category, and description. Data is saved to expenses.json and reloaded on startup.
2) List expenses
3) Total by category
4) Delete expense
5) Quit

Milestones - Finish each one before moving on.

1. In-memory version. 
Menu loop with while True, plus add and list. Store expenses as a list of dicts. Format output with f-strings.
2. Input validation. 
Reject non-numeric or negative amounts with try/except ValueError. Re-prompt instead of crashing.
3. Persistence. 
Save and load with the json module. Handle the first run, when the file doesn't exist yet (FileNotFoundError, or pathlib).
4. Reports. 
Total per category. Use a dict to accumulate, then print sorted from highest to lowest spend.
5. Delete by id. 
Make sure ids stay unique after deletions. Think about how to generate them.
6. Refactor into functions. One function per job (load_expenses, save_expenses, add_expense, etc.), with main() and an if __name__ == "__main__": guard.
'''
from datetime import date
import uuid
import json

class expense:
    def __init__(self, id: int, current_date: date, amount: float, category: str, desc: str):
        self.id = id
        self.current_date = current_date
        self.amount = amount
        self.category = category
        self.desc = desc

    def toDict(self):
        return {
            "id": self.id,
            "current_date": self.current_date,
            "amount": self.amount,
            "category": self.category,
            "dec": self.desc
        }

    def __str__(self):
        return f"Your {self.desc} expense was added on {self.current_date} and costs: {self.amount}"

class main:
    def generateShortID() -> str:
        return str(uuid.uuid4())[:6]
    
    today = date.today()
    list_of_expenses = []
    valid_input = ["exit", '1', '2', '3', '4', '5']
    n = True
    while n:
        user_input = input("What would you like to do? (1: Add expense 2: View expenses 3: Total By Category 4: Delete Expense 5: type'exit' to quit)")

        if user_input == "1":
            expense_amount = float(input("How much is the expense? "))
            expense_category = input("What category of expense is it? ")
            expense_desc = input("Enter a short description of the expense: ")
            new_expense = expense(generateShortID(), today, expense_amount, expense_category, expense_desc)
            list_of_expenses.append(new_expense)
            print("Expense added!")
            print(new_expense.id)
        elif user_input == "2":
            for e in list_of_expenses:
                print(f"Expense: {e}\n")
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else: 
            n = False

main()