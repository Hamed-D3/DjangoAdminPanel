from django.test import TestCase
from django.core.exceptions import ValidationError

from home.models import (
    GeneralSetting, 
    WebSiteSetting,
    AboutUsSetting,
    ContactUsSetting
)

class GeneralSettingTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       GeneralSetting.objects.create(name='setting')

    def test_correct_general_setting_name(self):
        general_setting = GeneralSetting.objects.all()[0]
        expected_object_name = 'setting'
        self.assertEqual(str(general_setting), expected_object_name)


class WebSiteSettingTest(TestCase):

    def setUp(self):
        self.general_setting = GeneralSetting.objects.create(name='setting')
        self.website_setting = WebSiteSetting.objects.create(
            name = "website setting",
            logo = 'default/logo.png',
            favico = 'default/ico.png',
            url = 'http://site.com',
            parent_setting = self.general_setting
        )

    def test_correct_website_setting_name(self):
        website_setting = WebSiteSetting.objects.get(id=1)
        expected_object_name = 'website setting'
        self.assertEqual(str(website_setting), expected_object_name)

    def test_validate_website_setting_have_only_one_instance_error(self):
        with self.assertRaises(ValidationError):
            website_setting = WebSiteSetting(
                name = "website setting2",
                logo = 'default/logo.png',
                favico = 'default/ico.png',
                url = 'http://site.com',
                parent_setting = self.general_setting
            )
            website_setting.full_clean()


class AboutUsSettingTest(TestCase):

    def setUp(self):
        self.general_setting = GeneralSetting.objects.create(name='setting')
        self.about_us_setting = AboutUsSetting.objects.create(
            about_us = "درباره ما",
            terms = "terms and condition",
            email = "info@site.com",
            phone = "+98 21 12345",
            addr = "addr",
            parent_setting = self.general_setting
        )

    def test_correct_about_us_setting_name(self):
        about_us_setting = AboutUsSetting.objects.get(id=1)
        expected_object_name = "درباره ما"
        self.assertEqual(str(about_us_setting), expected_object_name)

    def test_validate_about_us_setting_have_only_one_instance_error(self):
        with self.assertRaises(ValidationError):
            about_us_setting = AboutUsSetting(
                about_us = "درباره ما2",
                terms = "terms and condition",
                email = "info@site.com",
                phone = "+98 21 12345",
                addr = "addr",
                parent_setting = self.general_setting
            )
            about_us_setting.full_clean()


class ContactUsSettingTest(TestCase):

    def setUp(self):
        self.general_setting = GeneralSetting.objects.create(name='setting')
        self.contact_us_setting = ContactUsSetting.objects.create(
            contact_us = "تماس با ما",
            parent_setting = self.general_setting
        )

    def test_correct_contact_us_setting_name(self):
        contact_us_setting = ContactUsSetting.objects.get(id=1)
        expected_object_name = 'تماس با ما'
        self.assertEqual(str(contact_us_setting), expected_object_name)

    def test_validate_contact_us_setting_have_only_one_instance_error(self):
        with self.assertRaises(ValidationError):
            contact_us_setting = ContactUsSetting(
                contact_us = "تماس با ما2",
                parent_setting = self.general_setting
            )
            contact_us_setting.full_clean()