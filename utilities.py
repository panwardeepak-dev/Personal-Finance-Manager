from datetime import datetime


def get_amount():

    while True:

        try:

            amount = float(
                input("Enter Amount: ")
            )

            if amount <= 0:

                print("Amount must be greater than 0")

            else:

                return amount

        except ValueError:

            print("Please Enter a Valid Amount")


def get_date():

    return datetime.now().strftime("%Y-%m-%d")


def pause():

    input("\nPress Enter to continue...")