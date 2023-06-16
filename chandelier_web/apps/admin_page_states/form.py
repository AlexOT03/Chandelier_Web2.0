from django import forms
from .models import State

# create a ModelForm
class StateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = State
        fields = "__all__"
        # Exclude()
        # exclude = {}