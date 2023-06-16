from django import forms
from .models import Location, OpeningHour

# create a ModelForm
class LocationsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Location
        fields = "__all__"
        # Exclude()
        # exclude = {}
        
class OpeningHoursForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = OpeningHour
        # fields = "__all__"
        # Exclude()
        exclude = {'location'}