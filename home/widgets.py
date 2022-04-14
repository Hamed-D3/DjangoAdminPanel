from django.forms.widgets import ClearableFileInput

class CustomeClearableFileInput(ClearableFileInput):
    template_name = 'home/widgets/clearable_file_input.html'