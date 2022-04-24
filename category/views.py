from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView
)

from category.models import Category

from category.forms import CategoryModelForm

# Create your views here.
class CategoryListView(ListView):
    template_name = 'category/index.html'
    model = Category
    context_object_name = 'categories'


class CategoryCreateView(BSModalCreateView):
    template_name = 'category/create_category.html'
    form_class = CategoryModelForm
    success_message = 'موفق: دسته بندی با موفقیت ثبت شد.'
    success_url = reverse_lazy('category:category-list')


class CategoryUpdateView(BSModalUpdateView):
    model = Category
    template_name = 'category/update_category.html'
    form_class = CategoryModelForm
    success_message = 'موفق: دسته بندی با موفقیت ویرایش شد.'
    success_url = reverse_lazy('category:category-list')


class CategoryDeleteView(BSModalDeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_message = 'موفق: دسته بندی با موفقیت حذف شد.'
    success_url = reverse_lazy('category:category-list')