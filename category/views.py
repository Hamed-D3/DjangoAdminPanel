from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalCreateView

from category.models import Category

from category.forms import CategoryModelForm

# Create your views here.
class CategoryListView(ListView):
    template_name = 'category/index.html'
    model = Category
    context_object_name = 'categories'


class CategoryCreateView(BSModalCreateView):
    template_name = 'category/create_book.html'
    form_class = CategoryModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('category:category-list')