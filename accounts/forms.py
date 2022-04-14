from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from utils.widgets import CustomeClearableFileInput
from .models import User

class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
        widgets = {
            'avatar': CustomeClearableFileInput(),
        }