from bootstrap_modal_forms.forms import BSModalModelForm

from category.models import Category


class CategoryModelForm(BSModalModelForm):

    class Meta:
        model = Category
        fields = '__all__'