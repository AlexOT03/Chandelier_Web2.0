from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from . import models, form
from django.contrib import messages 

# Create your views here.
class LocationsView(LoginRequiredMixin, View):
    template_name = 'AdminLocations.html'

    def get(self, request, *args, **kwargs):
        ubicaciones = models.Location.objects.all()
        ubicacion_form = form.LocationsForm()
        HorarioFormSet = formset_factory(form.OpeningHoursForm, extra=7)
        horario_formset = HorarioFormSet()

        return render(request, self.template_name, {
            'locations': ubicaciones,
            'ubicacion_form': ubicacion_form,
            'horario_formset': horario_formset
        })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            ubicacion_form = form.LocationsForm(request.POST, request.FILES)
            HorarioFormSet = formset_factory(form.OpeningHoursForm, extra=7)
            horario_formSet = HorarioFormSet(request.POST)
            
            if ubicacion_form.is_valid():
                if horario_formSet.is_valid():
                    ubicacion = ubicacion_form.save()
                
                    horarios = horario_formSet.save(commit=False)
                    for horario in horarios:
                        horario.location = ubicacion
                        horario.save()
                    else:
                        print ("error en la base de datos")
            else:
                print("error detectado en el apartado ubicacion")
                
        return redirect('AdminLocations')