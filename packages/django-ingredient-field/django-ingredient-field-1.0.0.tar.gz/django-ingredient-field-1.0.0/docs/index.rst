.. django-ingredient-field documentation master file, created by
   sphinx-quickstart on Sun Aug 15 22:38:41 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-ingredient-field's documentation!
===================================================

Usage
=====

Simply add the field to your model::

   from dj_ingredient_field import IngredientField

   class MyModel(models.Model):
      ingredient = IngredientField()

The value of the field is an Ingredient object::

   from dj_ingredient_field import IngredientName, Ingredient

   model.ingredient = Ingredient(IngredientName.I_ARUGULA)

All the available ingredients can be found in the ``IngredientName`` enum

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
