from typing import Protocol

class PaymentProcessor(Protocol):

    def pay(self,amount: float) -> None:
        ...

class StripeProcessor(PaymentProcessor):

    def pay(self, amount: float) -> None:
        print(f"Payment of {amount} done using Stripe")
