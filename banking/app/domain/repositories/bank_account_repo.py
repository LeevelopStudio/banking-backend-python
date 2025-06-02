from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.bank_account import BankAccount

class BankAccountRepository(ABC):

    @abstractmethod
    def create(self, account: BankAccount) -> None:
        pass

    @abstractmethod
    def get(self, account_id: str) -> Optional[BankAccount]:
        pass

    @abstractmethod
    def delete(self, account_id: str) -> None:
        pass

    @abstractmethod
    def update(self, account: BankAccount) -> None:
        pass
