class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction( account, ammount_to_add):
        new_balance = account.balance + ammount_to_add
        if new_balance < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(ammount_to_add)
        return f"New balance: {new_balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __eq__(self, other):
        return self.amount == other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __add__(self, other):
        acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        for transaction in self._transactions:
            acc.add_transaction(transaction)
        for transaction in other._transactions:
            acc.add_transaction(transaction)
        return acc

    def __reversed__(self):
        return self._transactions[::-1]


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
