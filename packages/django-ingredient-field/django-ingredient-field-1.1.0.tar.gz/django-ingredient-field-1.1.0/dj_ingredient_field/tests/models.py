from dj_ingredient_field.fields import IngredientField
from django.db import models 

class TestModel(models.Model):
    ingredient = IngredientField()