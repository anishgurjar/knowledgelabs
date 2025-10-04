from current_payment_processor import PaymentProcessor
from legacy_integration import OldPayPal

class ProcessorAdapter(PaymentProcessor):

    _oldpaypal: OldPayPal

    def __init__(self, oldpaypal: OldPayPal):
        self._oldpaypal = oldpaypal
    
    def pay(self, amount) -> None:
        
        self._oldpaypal.makePaymentInCents(amount * 100)
        print(f"Payment of {amount} done using OldPayPal")