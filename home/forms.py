from django.forms import ModelForm
from utils.widgets import CustomeClearableFileInput

from .models import WebSiteSetting, AboutUsSetting, ContactUsSetting

class WebSiteSettingForm(ModelForm):

    class Meta:
        model = WebSiteSetting
        exclude = ('parent_setting', 'slug')
        widgets = {
            'logo': CustomeClearableFileInput(),
            'favico': CustomeClearableFileInput(),
        }


class AboutUsSettingForm(ModelForm):

    class Meta:
        model = AboutUsSetting
        exclude = ('parent_setting', 'slug')


class ContactUsSettingForm(ModelForm):

    class Meta:
        model = ContactUsSetting
        exclude = ('parent_setting', 'slug')