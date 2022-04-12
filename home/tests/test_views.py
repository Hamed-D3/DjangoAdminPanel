from django.test import TestCase
from django.urls import reverse_lazy
from home.models import GeneralSetting, WebSiteSetting

class IndexViewTest(TestCase):

    def test_show_home_page_correctly(self):
        response = self.client.get(reverse_lazy('home:index'))
        self.assertEqual(response.status_code, 200)

    def test_context_setting_name(self):
        response = self.client.get(reverse_lazy('home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('setting' in response.context)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy('home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/welcome.html')

    def test_context_with_create_website_setting(self):
        general_setting = GeneralSetting.objects.create(name='setting')
        website_setting = WebSiteSetting.objects.create(parent_setting=general_setting)
        response = self.client.get(reverse_lazy('home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('setting' in response.context)