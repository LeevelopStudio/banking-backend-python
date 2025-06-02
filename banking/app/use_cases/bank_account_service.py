from app.domain.repositories.bank_account_repo import BankAccountRepository
from app.domain.entities.bank_account import BankAccount

class BankAccountService:
    def __init__(self, repo: BankAccountRepository):
        self.repo = repo

    def create_account(self, owner: str) -> BankAccount:
        account = BankAccount(owner=owner)
        self.repo.create(account)
        return account

    def get_account(self, account_id: str) -> BankAccount:
        account = self.repo.get(account_id)
        if not account:
            raise ValueError("Account not found")
        return account

    def deposit(self, account_id: str, amount: float) -> BankAccount:
        account = self.get_account(account_id)
        account.deposit(amount)
        self.repo.update(account)
        return account

    def withdraw(self, account_id: str, amount: float) -> BankAccount:
        account = self.get_account(account_id)
        account.withdraw(amount)
        self.repo.update(account)
        return account

    def delete_account(self, account_id: str):
        self.repo.delete(account_id)