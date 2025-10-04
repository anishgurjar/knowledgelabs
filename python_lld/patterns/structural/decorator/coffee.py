from typing import Protocol

class Beverage(Protocol):

    _cost: float

    def cost(self) -> float:
        ...

    def description(self) -> str:
        ...

class DripCoffee(Beverage):

    _roast: str = "MEDIUM"
    _cost: float = 2.5

    def cost(self) -> float:
        return self._cost

    def description(self) -> str:
        return f"standard drip coffee (roast: {self._roast})"

    def set_roast(self, roast: str) -> None:
        if roast not in {"LIGHT","MEDIUM","DARK"}:
            raise ValueError("invalid roast")
        self._roast = roast

class SingleOriginEspresso(Beverage):

    _roast: str = "MEDIUM"

    def cost(self) -> float:
        return 2.5

    def description(self) -> str:
        return f"standard espresso (roast: {self._roast})"

    def set_roast(self, roast: str) -> None:
        if roast != "LIGHT" or roast != "MEDIUM" or roast != "DARK":
            raise ValueError("invalid roast")
        self._roast = roast

