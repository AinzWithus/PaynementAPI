from app.fake_payment_repository import FakePaymentRepository


def test_save_payment():

    repo = FakePaymentRepository()

    payment = {
        "id": "pay_1",
        "customer_id": "cust_001",
        "amount": 100,
        "currency": "USD",
        "status": "pending"
    }

    repo.save_payment(payment)

    result = repo.find_payment_by_id("pay_1")

    assert result["amount"] == 100


def test_find_payments_by_customer():

    repo = FakePaymentRepository()

    payment1 = {
        "id": "pay_1",
        "customer_id": "cust_001",
        "amount": 100,
        "currency": "USD",
        "status": "pending"
    }

    payment2 = {
        "id": "pay_2",
        "customer_id": "cust_001",
        "amount": 200,
        "currency": "USD",
        "status": "pending"
    }

    repo.save_payment(payment1)
    repo.save_payment(payment2)

    payments = repo.find_payments_by_customer("cust_001")

    assert len(payments) == 2


def test_save_refund():

    repo = FakePaymentRepository()

    refund = {
        "payment_id": "pay_1",
        "amount": 50
    }

    repo.save_refund(refund)

    refunds = repo.find_refunds_by_payment("pay_1")

    assert refunds[0]["amount"] == 50