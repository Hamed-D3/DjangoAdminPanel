from django.test import TestCase
from django.core.exceptions import ValidationError

from accounts.models import User

class UserTestModel(TestCase):
    def setUp(self):
        self.password = 'epro30@#2c'
        self.user = User.objects.create(
            email='site@site.com',
            password=self.password,
            phone='09111231111',
            avatar='default/user.png'
        )

    def test_show_avatar(self):
        expect_avatar_tag = f"<img src='/media/default/user.png' width='30' height='30'>"
        self.assertEqual(self.user.show_avatar(), expect_avatar_tag)

    def test_validate_iran_phone_number_error(self):
        invalid_phone = '9111231234'
        with self.assertRaises(ValidationError):
            user = User(
                email='user@site.com',
                password=self.password,
                phone= invalid_phone
            )
            user.full_clean()

    def test_validate_iran_phone_number(self):
        valid_phone = ['+989111231234', '00989111231235', '09111231236']
        for i, phone in enumerate(valid_phone, 1):
            user = User(
                email=f'user{i}@site.com',
                username=f'user{i}',
                password=self.password,
                phone=phone
            )
            user.full_clean()

    def test_email_user_exist_error(self):
        with self.assertRaises(ValidationError):
            user = User(
                email='site@site.com',
                password=self.password,
            )
            user.full_clean()
    
    def test_phone_user_exist_error(self):
        duplicate_phone='09111231111'
        with self.assertRaises(ValidationError):
            user = User(
                email='user@site.com',
                password=self.password,
                phone=duplicate_phone
            )
            user.full_clean()

    def test_create_user(self):
        user = User.objects.create_user(
            email='user@site.com',
            username='user',
            password=self.password,
        )
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email='user@site.com',
            username='superuser',
            password=self.password,
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_without_email_error(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                email='',
                username='user',
                password=self.password,
            )
            user.full_clean()

    def test_create_superuser_with_is_staff_false_error(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_superuser(
                email='user@site.com',
                username='user',
                password=self.password,
                is_staff=False
            )
            user.full_clean()

    def test_create_superuser_with_is_superuser_false_error(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_superuser(
                email='user@site.com',
                username='user',
                password=self.password,
                is_superuser=False
            )
            user.full_clean()