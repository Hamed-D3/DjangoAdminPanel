from django.test import TestCase

from role.models import Role, Permission


class PermissionModelTest(TestCase):
    def setUp(self):
        Permission.objects.create(
            name = 'permission',
            show_name = 'permission_name'
        )

    def test_model_str(self):
        permission = Permission.objects.get(pk=1)
        expected_object_name = 'permission_name'
        self.assertEqual(str(permission), expected_object_name)


class RoleModelTest(TestCase):

    def setUp(self):
        self.permission_one = Permission.objects.create(
            name = 'permission',
            show_name = 'permission_name'
        )
        self.permission_two = Permission.objects.create(
            name = 'permission2',
            show_name = 'permission_name2'
        )
        self.role = Role.objects.create(name = 'role')
        self.role.permission.set([self.permission_one.pk, self.permission_two.pk])

    def test_model_str(self):
        role = Role.objects.get(pk=1)
        expected_object_name = 'role'
        self.assertEqual(str(role), expected_object_name)

    def test_show_permission_names_method(self):
        role = Role.objects.all()[0]
        expected_object_name = '، '.join([str(self.permission_one), str(self.permission_two)])
        self.assertEqual(role.show_permission_name(), expected_object_name)