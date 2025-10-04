from coffee import SingleOriginEspresso
from add_ons import Milk, ChocolateSyrup

mylatte = ChocolateSyrup(Milk(SingleOriginEspresso()))

print(mylatte.cost())
print(mylatte.description())

