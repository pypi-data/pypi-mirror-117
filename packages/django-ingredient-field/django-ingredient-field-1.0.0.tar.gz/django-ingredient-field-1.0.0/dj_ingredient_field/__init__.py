__version__ = "1.0.0"

from .fields import IngredientField
from .enums import IngredientName

class Ingredient():
    def __init__(self, name : IngredientName ) -> None:
        self.name = str(name)
        print(self)

    def __str__(self):
        return str(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Ingredient) and o.name == self.name

