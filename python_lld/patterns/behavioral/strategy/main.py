from typing import Protocol

class PaymentMethod(Protocol):
    def pay(amount: float) -> None:
        ...

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Payment of ${amount} has been deducted from credit card")

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Payment of ${amount} has been deducted from paypal")

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Payment of ${amount} has been deducted from crypto wallet")

class PaymentProcessor:

    _paymentMethod: PaymentMethod

    def __init__(self, payment_method: PaymentMethod):
        self._paymentMethod = payment_method

    def setPaymentMethod(payment_method: PaymentMethod):
        self._paymentMethod = payment_method
    
    def pay(self, amount: float):
        self._paymentMethod.pay(amount)


creditCardPayment = CreditCardPayment()
p1 = PaymentProcessor(creditCardPayment)
p1.pay(100)


