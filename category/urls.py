from django.urls import path
from category.views import IndexView

app_name = 'category'
urlpatterns = [
    path('categories/', IndexView.as_view(), name='category'),
]