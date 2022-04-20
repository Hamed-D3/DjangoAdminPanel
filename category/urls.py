from django.urls import path
from category.views import (
    CategoryListView, 
    CategoryCreateView,
)

app_name = 'category'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('create/', CategoryCreateView.as_view(), name='category-create'),
]