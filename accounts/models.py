from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, validate_image_file_extension
from django.utils.html import format_html
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


IRAN_PHONE_NUMBER_VALIDATOR = RegexValidator(r'^(0098|\+?98|0)9\d{9}$', message="لطفا شماره موبایل معتبر وارد نمایید")


class User(AbstractUser):
    # # remove username and email required
    # username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(_('email address'), unique=True)

    # add new field
    phone = models.CharField(max_length=15, unique=True, blank=True, validators=[IRAN_PHONE_NUMBER_VALIDATOR], verbose_name="شماره موبایل")
    avatar = models.ImageField(upload_to='avatars/', default='default/user.png', validators=[validate_image_file_extension], verbose_name="عکس پروفایل")


    def show_avatar(self):
        return format_html(f"<img src='{self.avatar.url}' width='30' height='30'>")
    show_avatar.short_description = 'عکس پروفایل'

    objects = UserManager()