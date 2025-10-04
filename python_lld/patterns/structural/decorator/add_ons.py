from coffee import Beverage
from typing import Protocol

class BeverageDecorator(Protocol):
    
    _beverage: Beverage
    _extracost: float

    def cost(self) -> float:
        ...

    def description(self) -> str:
        ...

class Milk(BeverageDecorator):
    
    _beverage: Beverage
    _extracost: float = 1

    def __init__(self, beverage: Beverage ):
        self._beverage = beverage

    def cost(self) -> float:
        return self._beverage.cost() + self._extracost

    def description(self) -> str:
        return self._beverage.description() + " + Milk"

class ChocolateSyrup(BeverageDecorator):
    
    _beverage: Beverage
    _extracost: float = 2

    def __init__(self, beverage: Beverage ):
        self._beverage = beverage

    def cost(self) -> float:
        return self._beverage.cost() + self._extracost

    def description(self) -> str:
        return self._beverage.description() + " + Chocolate Syrup"
