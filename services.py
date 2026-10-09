import json
import csv

from models import Transaction
from utilities import get_amount, get_date


DATA_FILE = "data/transactions.json"


def add_income(transactions):

    print("\n========== ADD INCOME ==========")

    amount = get_amount()
    category = input("Enter Category: ").strip()
    description = input("Enter Description: ").strip()
    date = get_date()

    transaction = Transaction(
        "income",
        amount,
        category,
        description,
        date
    )

    transactions.append(transaction)

    print("Income Added Successfully")


def add_expense(transactions):

    print("\n========== ADD EXPENSE ==========")

    amount = get_amount()
    category = input("Enter Category: ").strip()
    description = input("Enter Description: ").strip()
    date = get_date()

    transaction = Transaction(
        "expense",
        amount,
        category,
        description,
        date
    )

    transactions.append(transaction)

    print("Expense Added Successfully")


def view_transactions(transactions):

    print("\n========== ALL TRANSACTIONS ==========")

    if len(transactions) == 0:
        print("No Transactions Found")
        return

    for index, transaction in enumerate(transactions, start=1):

        transaction.display(index)

        print("-" * 40)


def search_transactions(transactions):

    print("\n========== SEARCH TRANSACTIONS ==========")

    if len(transactions) == 0:
        print("No Transactions Found")
        return

    keyword = input("Enter Search Keyword: ").lower()

    found = False

    for index, transaction in enumerate(transactions, start=1):

        if (
            keyword in transaction.category.lower()
            or keyword in transaction.description.lower()
        ):

            transaction.display(index)

            print("-" * 40)

            found = True

    if not found:
        print("No Matching Transactions Found")


def filter_by_category(transactions):

    print("\n========== FILTER BY CATEGORY ==========")

    if len(transactions) == 0:
        print("No Transactions Found")
        return

    category = input("Enter Category: ").lower()

    found = False

    for index, transaction in enumerate(transactions, start=1):

        if transaction.category.lower() == category:

            transaction.display(index)

            print("-" * 40)

            found = True

    if not found:
        print("No Transactions Found For This Category")


def total_income(transactions):

    total = 0

    for transaction in transactions:

        if transaction.transaction_type == "income":
            total += transaction.amount

    print("\nTotal Income: ₹", total)


def total_expenses(transactions):

    total = 0

    for transaction in transactions:

        if transaction.transaction_type == "expense":
            total += transaction.amount

    print("\nTotal Expenses: ₹", total)


def current_balance(transactions):

    income = 0
    expense = 0

    for transaction in transactions:

        if transaction.transaction_type == "income":
            income += transaction.amount

        elif transaction.transaction_type == "expense":
            expense += transaction.amount

    balance = income - expense

    print("\n========== CURRENT BALANCE ==========")
    print("Total Income: ₹", income)
    print("Total Expenses: ₹", expense)
    print("Current Balance: ₹", balance)


def save_data(transactions):

    try:

        data = []

        for transaction in transactions:
            data.append(transaction.to_dict())

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Data Saved Successfully")

    except Exception as e:

        print("Error While Saving Data:", e)


def load_data():

    try:

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        transactions = []

        for item in data:

            transaction = Transaction.from_dict(item)

            transactions.append(transaction)

        print("Data Loaded Successfully")

        return transactions

    except FileNotFoundError:

        print("No Saved Data Found")

        return []

    except json.JSONDecodeError:

        print("Invalid JSON File")

        return []


def export_csv(transactions):

    if len(transactions) == 0:

        print("No Transactions To Export")

        return

    try:

        with open(
            "data/transactions.csv",
            "w",
            newline=""
        ) as file:

            fieldnames = [
                "type",
                "amount",
                "category",
                "description",
                "date"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for transaction in transactions:

                writer.writerow(
                    transaction.to_dict()
                )

        print("Data Exported Successfully")

    except Exception as e:

        print("Error While Exporting Data:", e)