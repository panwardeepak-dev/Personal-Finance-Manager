class Transaction:

    def __init__(self, transaction_type, amount, category, description, date):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["type"],
            data["amount"],
            data["category"],
            data["description"],
            data["date"]
        )

    def display(self, index=None):

        if index is not None:
            print(f"\nTransaction #{index}")

        print("Type:", self.transaction_type)
        print("Amount: ₹", self.amount)
        print("Category:", self.category)
        print("Description:", self.description)
        print("Date:", self.date)