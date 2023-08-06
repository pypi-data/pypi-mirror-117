from dj_ingredient_field import IngredientField, IngredientName, Ingredient
from django.test import TestCase

# Create your tests here.
class IngredientFieldTests(TestCase):

    def test_create_test_model(self):
        from .models import TestModel

        TestModel(ingredient=Ingredient(IngredientName.I_ADOBO)).save()

        TestModel.objects.get(pk=1)

    def test_assign_retrieve_value(self):
        from .models import TestModel
        t_model = TestModel(ingredient=Ingredient(IngredientName.I_ADOBO))
        t_model.save()

        self.assertEquals(t_model.ingredient, Ingredient(IngredientName.I_ADOBO), "Incorrect ingredient assigned")
        t_model.ingredient = Ingredient(IngredientName.I_VODKA)
        t_model.save()

        self.assertEquals(t_model.ingredient, Ingredient(IngredientName.I_VODKA), "Incorrect ingredient assigned")

    def test_retrieve_value_is_type_ingredient(self):
        from .models import TestModel
        t_model = TestModel(ingredient=Ingredient(IngredientName.I_ADOBO))
        t_model.save()

        self.assertIsInstance(t_model.ingredient, Ingredient, "Incorrect ingredient type on retrieveal")

    def test_deconstruct_no_args(self):
        from .models import TestModel
        self.assertEqual(
            (None,'dj_ingredient_field.fields.IngredientField',[],{}),
            IngredientField().deconstruct(), "deconstructed values were not empty or something went wrong")

    def test_deconstruct_test_args(self):
        self.assertEqual(
            (None,'dj_ingredient_field.fields.IngredientField',[],{'blank': True, 'null': True}),
            IngredientField(blank=True,null=True).deconstruct(), "deconstructed values were missing or something went wrong")

    def test_deconstruct_no_max_length(self):
        _,_,_,kwargs = IngredientField().deconstruct()
        self.assertFalse('max_length' in kwargs, 'max_length was deconstructed as a kwarg')

    def test_deconstruct_no_choices(self):
        _,_,_,kwargs = IngredientField().deconstruct()
        self.assertFalse('choices' in kwargs, 'choices was deconstructed as a kwarg')