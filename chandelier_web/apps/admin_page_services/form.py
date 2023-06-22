from django import forms
from .models import Service
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class ServicesForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Service
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "description": _("Descripcion"),
            "price": _("Precio"),
            "duration": _("Duracion")
        }
        help_texts = {
            # "name": _("Nombre"),
            "duration": _("00:00")
        }
        error_messages = {
            # "name": {
            #     "max_length": _("El texto es demaciado largo"),
            # },
        }