from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from . import models, form

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
            ubicacion_form = form.LocationsForm(request.POST)
            HorarioFormSet = formset_factory(form.OpeningHoursForm, extra=7)
            horario_formset = HorarioFormSet(request.POST)
            
            if ubicacion_form.is_valid() and horario_formset.is_valid():
                 # Guardar la ubicación en la base de datos
                print('sucess en la base de datos 1')
                ubicacion = ubicacion_form.save()

                # Guardar los horarios en la base de datos asociados a la ubicación
                for horario_form in horario_formset:
                    horario = horario_form.save(commit=False)
                    horario.location = ubicacion
                    print('sucess en la base de datos 2')
                    horario.save()

            return redirect('AdminLocations')  # Redireccionar a la página deseada después de guardar

        return render(request, self.template_name, {
            'ubicacion_form': ubicacion_form,
            'horario_formset': horario_formset
        })