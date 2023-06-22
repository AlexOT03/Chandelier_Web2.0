from django import forms
from .models import Location, OpeningHour
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class LocationsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Location
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "owner": _("Dueño"),
            "location": _("Ubicacion"),
            "location_length": _("Largo"),
            "location_width": _("Ancho"),
            "state": _("Estado"),
            "theme": _("Tematica"),
            "capacity": _("Cupo"),
            "created_date": _("Fecha de registro"),
            "price": _("Precio"),
            "description": _("Descripción"),
            "images": _("Imagen"),
        }
        help_texts = {
            # "name": _("Nombre"),
            # "owner": _("Dueño"),
            # "location": _("Ubicacion"),
            # "location_length": _("Largo"),
            # "location_width": _("Ancho"),
            # "state": _("Estado"),
            # "theme": _("Tematica"),
            # "capacity": _("Cupo"),
            # "created_date": _("Fecha de alta"),
            # "price": _("Precio"),
            # "description": _("Descripción"),
            # "images": _("Imagen"),
        }
        error_messages = {
            # "name": {
            #     "max_length": _("El texto es demaciado largo"),
            # },
        }
        
class MyTimeInput(forms.widgets.TimeInput):
    input_type = 'time'
        
class OpeningHoursForm(forms.ModelForm):
    # specify the name of model to use
    opening_time = forms.TimeField(widget=MyTimeInput())
    closing_time = forms.TimeField(widget=MyTimeInput())
    class Meta:
        model = OpeningHour
        exclude = {'location'}
        labels = {
            "location": _("Ubicacion"),
            "day_of_week": _("Dia"),
            "opening_time": _("Apertura"),
            "closing_time": _("Cierre"),
        }
        help_texts = {
            # "location": _("Ubicacion"),
            # "day_of_week": _("Dia"),
            # "opening_time": _("Apertura"),
            # "closing_time": _("Cierre"),
        }
        error_messages = {
            # "location": {
            #     "max_length": _("El texto es demaciado largo"),
            # },
        }