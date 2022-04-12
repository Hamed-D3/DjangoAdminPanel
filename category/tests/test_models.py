from django.test import TestCase

from category.models import Category

class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title="title")


    def test_model_str(self):
        category = Category.objects.get(pk=1)
        expected_object_name = 'title'
        self.assertEqual(str(category), expected_object_name)