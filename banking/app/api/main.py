# app/api/main.py
from fastapi import FastAPI
from app.adapters.repositories.sqlalchemy_bank_account import SQLAlchemyBankAccountRepository
from app.use_cases.bank_account_service import BankAccountService
from app.api.routes import bank_account_routes

app = FastAPI()
repo = SQLAlchemyBankAccountRepository(None)
bank_account_routes.service = BankAccountService(repo)
app.include_router(bank_account_routes.router)