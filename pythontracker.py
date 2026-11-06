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
Save and load with the json module. Handle the first run, when the file doesn’t exist yet (FileNotFoundError, or pathlib).
4. Reports. 
Total per category. Use a dict to accumulate, then print sorted from highest to lowest spend.
5. Delete by id. 
Make sure ids stay unique after deletions. Think about how to generate them.
6. Refactor into functions. One function per job (load_expenses, save_expenses, add_expense, etc.), with main() and an if __name__ == "__main__": guard.
'''
from datetime import date

class expense:
    def __init__(self, id: int, currentDate: date, amount: int, category: str, desc: str):
        self.id = id
        self.currentDate = currentDate
        self.amount = amount
        self.category = category
        self.desc = desc

    def to_dict(self):
        return {
            "id": self.id,
            "currentDate": date,
            "amount": self.amount,
            "category": self.category,
            "dec": self.desc
        }

class main:
    n = True
    while n:
        userInput = input("What would you like to do? (1: Add expense 2: View expenses 3: Total By Category 4: Delete Expense 5: type'exit' to quit)")

        if userInput == 1:
            
            newExpense = expense()
        elif userInput == 2:
            pass
        elif userInput == 3:
            pass
        elif userInput == 4:
            pass
        else:
            n = False