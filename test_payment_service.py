import pytest
from app.payment_service import PaymentService
from app.fake_payment_repository import FakePaymentRepository
from app.customers import customers


def test_create_payment():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    payment = service.create_payment("cust_001", 100, "USD")

    assert payment["amount"] == 100
    assert payment["currency"] == "USD"


def test_create_payment_invalid_customer():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    with pytest.raises(ValueError):
        service.create_payment("cust_999", 100, "USD")


def test_get_payment():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    payment = service.create_payment("cust_001", 100, "USD")

    result = service.get_payment(payment["id"])

    assert result["id"] == payment["id"]


def test_capture_payment():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    payment = service.create_payment("cust_001", 100, "USD")

    captured = service.capture(payment["id"])

    assert captured["status"] == "captured"


def test_refund_payment():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    payment = service.create_payment("cust_001", 100, "USD")

    service.capture(payment["id"])

    refund = service.refund(payment["id"], 50)

    assert refund["amount"] == 50


def test_refund_exceed_payment():

    repo = FakePaymentRepository()
    service = PaymentService(repo, customers)

    payment = service.create_payment("cust_001", 100, "USD")

    service.capture(payment["id"])

    with pytest.raises(ValueError):
        service.refund(payment["id"], 200)