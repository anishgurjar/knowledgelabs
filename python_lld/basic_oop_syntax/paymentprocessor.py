from typing import Protocol, NoReturn

class PaymentStrategy(Protocol):
    def pay(self, amount: int) -> NoReturn:
        ...

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> NoReturn:
        print("payment charged on credit card strategy")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: int) -> NoReturn:
        print("payment charged on PayPal strategy")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount: int) -> NoReturn:
        print("payment charged on Crypto strategy")

class Checkout:
    
    _strategy: PaymentStrategy

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def pay(self, amount: int) -> NoReturn:
        self._strategy.pay(amount)
    
    def setPaymentStrategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

paypal = PayPalPayment()
myCheckout = Checkout(paypal)
myCheckout.pay(1000)