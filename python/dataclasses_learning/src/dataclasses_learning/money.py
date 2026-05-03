
from dataclasses import dataclass

@dataclass
class Money: 

    def __init__(self, amount: int, current: str):
        if amount < 0:
            raise ValueError(f"Invalid amount {amount}. Amount must be greater than 0")
        self.amount = amount
        self.currency = current

if __name__ == "__main__":
    m = Money(100, "USD")
    m1 = Money(100, "USD")
    print(f"{m1 == m}")