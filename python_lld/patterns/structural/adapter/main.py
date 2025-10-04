from current_payment_processor import StripeProcessor
from legacy_integration import OldPayPal
from adapter import ProcessorAdapter

stripe_processor = StripeProcessor()
old_paypal_processor = ProcessorAdapter(OldPayPal())


stripe_processor.pay(1000) #old code works just fine
old_paypal_processor.pay(1000) #old code works just fine

