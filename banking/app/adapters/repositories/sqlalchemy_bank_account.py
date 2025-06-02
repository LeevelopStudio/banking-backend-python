from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entities.bank_account import BankAccount
from app.domain.repositories.bank_account_repo import BankAccountRepository

class SQLAlchemyBankAccountRepository(BankAccountRepository):
    def __init__(self, session: Session):
        self.session = session
        self._db = {}  # Using dict as mock DB

    def create(self, account: BankAccount) -> None:
        self._db[account.id] = account

    def get(self, account_id: str) -> Optional[BankAccount]:
        return self._db.get(account_id)

    def delete(self, account_id: str) -> None:
        if account_id in self._db:
            del self._db[account_id]

    def update(self, account: BankAccount) -> None:
        self._db[account.id] = account
