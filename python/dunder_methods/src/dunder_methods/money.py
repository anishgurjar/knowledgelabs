class Money:

    def __init__(self, amount: int, currency: str):
        if self.amount < 0:
            raise ValueError(f"Invalid amount {amount}. Amount must be greater than 0")
        self.amount = amount
        self.currency = currency
    
    def __repr__(self) -> str:
        return f"{self.__class__} Amount: {self.amount}, Currency: {self.currency}"
    
    def __add__(self, other: Money) -> Money:
        if other.currency != self.currency:
            raise ValueError("Currency of both Money should be the same")
        return Money(self.amount + other.amount, self.currency)
