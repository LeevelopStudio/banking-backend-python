from dataclasses import dataclass, field
import uuid

@dataclass
class BankAccount:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    owner: str = ""
    balance: float = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
