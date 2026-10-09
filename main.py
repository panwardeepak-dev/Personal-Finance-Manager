from services import (
    add_income,
    add_expense,
    view_transactions,
    search_transactions,
    filter_by_category,
    total_income,
    total_expenses,
    current_balance,
    save_data,
    load_data,
    export_csv
)

from utilities import pause


def show_menu():

    print("\n")
    print("=" * 45)
    print("       PERSONAL FINANCE MANAGER")
    print("=" * 45)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Search Transactions")
    print("5. Filter by Category")
    print("6. Total Income")
    print("7. Total Expenses")
    print("8. Current Balance")
    print("9. Export Data")
    print("10. Exit")


def main():

    transactions = load_data()

    while True:

        show_menu()

        choice = input("\nEnter Your Choice: ")

        if choice == "1":

            add_income(transactions)

            save_data(transactions)

            pause()

        elif choice == "2":

            add_expense(transactions)

            save_data(transactions)

            pause()

        elif choice == "3":

            view_transactions(transactions)

            pause()

        elif choice == "4":

            search_transactions(transactions)

            pause()

        elif choice == "5":

            filter_by_category(transactions)

            pause()

        elif choice == "6":

            total_income(transactions)

            pause()

        elif choice == "7":

            total_expenses(transactions)

            pause()

        elif choice == "8":

            current_balance(transactions)

            pause()

        elif choice == "9":

            export_csv(transactions)

            pause()

        elif choice == "10":

            save_data(transactions)

            print("\nThank You for Using Personal Finance Manager!")

            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()