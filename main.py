from fastapi import FastAPI
from app.payment_service import PaymentService
from app.fake_payment_repository import FakePaymentRepository
from app.customers import customers

app = FastAPI()

repo = FakePaymentRepository()
service = PaymentService(repo, customers)


@app.post("/payments")
def create_payment(customer_id: str, amount: int, currency: str):

    return service.create_payment(customer_id, amount, currency)


@app.get("/payments/{payment_id}")
def get_payment(payment_id: str):

    return service.get_payment(payment_id)


@app.post("/payments/{payment_id}/capture")
def capture(payment_id: str):

    return service.capture(payment_id)


@app.post("/payments/{payment_id}/refund")
def refund(payment_id: str, amount: int):

    return service.refund(payment_id, amount)