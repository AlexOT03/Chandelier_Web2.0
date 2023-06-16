from django import forms
from .models import Service

# create a ModelForm
class ServicesForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Service
        fields = "__all__"
        # Exclude()
        # exclude = {}