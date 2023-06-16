from django import forms
from .models import Theme

# create a ModelForm
class ThemeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Theme
        fields = "__all__"
        # Exclude()
        # exclude = {}