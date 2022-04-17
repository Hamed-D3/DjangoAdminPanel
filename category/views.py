from django.views.generic import ListView
from category.models import Category

# Create your views here.
class CategoryListView(ListView):
    template_name = 'category/index.html'
    model = Category
    context_object_name = 'categories'