from django import forms
from .models import State
from PIL import Image
from django.utils.translation import gettext_lazy as _

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "description": _("Descripcion"),
            "images": _("Imagen"),
        }
        help_texts = {
            # "name": _("Nombre"),
        }
        error_messages = {
            # "name": {
            #     "max_length": _("El texto es demaciado largo"),
            # },
        }
        
    def clean_images(self):
        images = self.cleaned_data.get('images', False)
    
        if images:
            desired_width = 1000
            desired_height = 1000
    
            # Abrir la imagen utilizando PIL
            img = Image.open(images)
    
            width, height = img.size
    
            if width > desired_width or height > desired_height:
                # img.resize(( desired_width, desired_height))
                # images = img
                
                # return images
                
                raise forms.ValidationError(
                    f"La imagen debe tener una anchura mínima de {desired_width}px y una altura mínima de {desired_height}px."
                )
    
        return images