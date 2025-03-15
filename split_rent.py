import csv

class Roommate:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
        self.expenses = []
    
    def add_expense(self, description, amount):
        self.expenses.append((description, amount))
    
    def total_expenses(self):
        return sum(amount for _, amount in self.expenses)
    
    def __str__(self):
        return f"{self.name} ({self.percentage}% share)"

def calculate_split(total_rent, roommates):
    rent_distribution = {}
    for roommate in roommates:
        rent_distribution[roommate.name] = (roommate.percentage / 100) * total_rent
    return rent_distribution

def display_summary(total_rent, roommates):
    print("\n--- Rent and Expense Summary ---")
    rent_split = calculate_split(total_rent, roommates)
    for roommate in roommates:
        print(f"{roommate.name} owes: ${rent_split[roommate.name]:.2f}")
        if roommate.expenses:
            print("  Individual Expenses:")
            for description, amount in roommate.expenses:
                print(f"    - {description}: ${amount:.2f}")
        print(f"  Total personal expenses: ${roommate.total_expenses():.2f}\n")
    print("--- End of Summary ---")

def load_roommates(filename):
    roommates = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, percentage = row
            roommates.append(Roommate(name, float(percentage)))
    return roommates

def load_expenses(filename, roommates):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, description, amount = row
            for roommate in roommates:
                if roommate.name == name:
                    roommate.add_expense(description, float(amount))

def main():
    total_rent = float(input("Enter total rent amount: $"))
    roommates = load_roommates("roommates.csv")
    load_expenses("expenses.csv", roommates)
    display_summary(total_rent, roommates)

if __name__ == "__main__":
    main()
