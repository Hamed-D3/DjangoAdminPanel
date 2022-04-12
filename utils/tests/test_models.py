# from django.test import TestCase

# from utils.models import SoftDeleteModel


# class SoftDeleteModelTest(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         SoftDeleteModel.objects.create(pk=1)

#     def test_soft_delete_method_manager(self):
#         SoftDeleteModel.objects.get(pk=1).soft_delete()
#         q = SoftDeleteModel.objects.get(pk=1).deleted_at()
#         self.assertIsNotNone(q)

#     def test_soft_restore_method_manager(self):
#         SoftDeleteModel.objects.get(pk=1).soft_restore()
#         q = SoftDeleteModel.objects.get(pk=1).deleted_at()
#         self.assertIsNone(q)


# link for help: https://stackoverflow.com/questions/4281670/django-best-way-to-unit-test-an-abstract-model/