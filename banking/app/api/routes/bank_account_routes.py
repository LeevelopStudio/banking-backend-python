# app/api/routes/bank_account_routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.use_cases.bank_account_service import BankAccountService

router = APIRouter()

class CreateAccountRequest(BaseModel):
    owner: str

class AmountRequest(BaseModel):
    amount: float

service: BankAccountService = None  # Will be injected

@router.post("/accounts")
def create_account(data: CreateAccountRequest):
    account = service.create_account(data.owner)
    return account

@router.get("/accounts/{account_id}")
def get_account(account_id: str):
    try:
        return service.get_account(account_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/accounts/{account_id}/deposit")
def deposit(account_id: str, data: AmountRequest):
    try:
        return service.deposit(account_id, data.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: str, data: AmountRequest):
    try:
        return service.withdraw(account_id, data.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    service.delete_account(account_id)
    return {"status": "deleted"}
