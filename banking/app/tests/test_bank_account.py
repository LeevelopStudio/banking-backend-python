from fastapi.testclient import TestClient
from api.main import app  # assuming PYTHONPATH is set to app/src

client = TestClient(app)

def test_create_account():
    response = client.post("/accounts", json={"owner": "Alice"})
    assert response.status_code == 200
    data = response.json()
    assert data["owner"] == "Alice"
    assert data["balance"] == 0.0
    return data["id"]

def test_deposit_withdraw_and_balance():
    account_id = test_create_account()

    # Deposit
    deposit_resp = client.post(f"/accounts/{account_id}/deposit", json={"amount": 100.0})
    assert deposit_resp.status_code == 200
    assert deposit_resp.json()["balance"] == 100.0

    # Withdraw
    withdraw_resp = client.post(f"/accounts/{account_id}/withdraw", json={"amount": 40.0})
    assert withdraw_resp.status_code == 200
    assert withdraw_resp.json()["balance"] == 60.0

    # Get account
    get_resp = client.get(f"/accounts/{account_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["balance"] == 60.0

    # Delete account
    delete_resp = client.delete(f"/accounts/{account_id}")
    assert delete_resp.status_code == 200

    # Confirm deletion
    get_after_delete = client.get(f"/accounts/{account_id}")
    assert get_after_delete.status_code == 404
