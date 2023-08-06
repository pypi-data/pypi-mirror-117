from typing import Any, Optional, Union
from django.db import models
from django.forms.fields import ChoiceField
from dj_ingredient_field.enums import IngredientName
import math 

class IngredientField(models.CharField):
    """
    An ingredient field for Django models 
    which provides over 3500 cooking ingredients

    Dataset from https://dominikschmidt.xyz/simplified-recipes-1M/
    """
    description = "A cooking ingredient"

    def __init__(self, *args, **kwargs):
        
        kwargs['choices'] = IngredientName.choices
        kwargs['max_length'] =  math.ceil(math.log10(len(IngredientName.choices)))

        super().__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Removes choices and max_length keywords as these 
        are not to be user editable
        """
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        del kwargs['max_length']

        return name, path, args, kwargs 