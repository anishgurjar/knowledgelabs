#pizza builder
from typing import Protocol 


Crust = Literal["thin", "thick", "gluten_free"]
Sauce = Literal["tomato", "pesto", "white_garlic"]
Cheese = Literal["mozzarella", "vegan", "cheddar"]


class Pizza:

    def __init__(self, crust_type: str, topping: str[], sauces: str[], cheeses: str[], extras: str[], stuffed: str):

        self.crust_type = curst_type
        self.