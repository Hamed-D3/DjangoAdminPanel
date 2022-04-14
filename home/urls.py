from django.urls import path
from .views import IndexView, WebSiteSettingView, AboutUsSettingView, ContactUsSettingView

app_name = 'home'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('settings/general/<slug:slug>/', WebSiteSettingView.as_view(), name='website-setting'),
    path('settings/aboutus/<slug:slug>/', AboutUsSettingView.as_view(), name='aboutus-setting'),
    path('settings/contactus/<slug:slug>/', ContactUsSettingView.as_view(), name='contactus-setting'),
]