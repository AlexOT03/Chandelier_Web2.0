from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from .models import Location, OpeningHour
from .form import LocationsForm, OpeningHoursForm
from django.forms.models import modelformset_factory

# Create your views here.
class LocationsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        form_locations = LocationsForm()
        form_class = formset_factory(OpeningHoursForm, extra=0, min_num=7, validate_min=True)
        form_hours = form_class(initial=[
            {'day_of_week': 1},  # Lunes
            {'day_of_week': 2},  # Martes
            {'day_of_week': 3},  # Miércoles
            {'day_of_week': 4},  # Jueves
            {'day_of_week': 5},  # Viernes
            {'day_of_week': 6},  # Sábado
            {'day_of_week': 7},  # Domingo
        ])
        
        return render(request, 'AdminLocations.html', {
            'locations': locations,
            'form_locations': form_locations,
            'form_hours': form_hours,
        })
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            error_vr = None
            locations = Location.objects.all()
            form_locations = LocationsForm(request.POST, request.FILES)
            form_class = formset_factory(OpeningHoursForm, extra=7)
            form_hours = form_class(request.POST)
        
            if form_locations.is_valid() and form_hours.is_valid():
                location = form_locations.save()
                
                for form in form_hours:
                   hours = form.save(commit=False)
                   hours.location = location
                   hours.save()
            else:
                error_vr = "El formulario no es válido"
                return render(request, 'AdminLocations.html', {
                    'locations': locations,
                    'form_locations': form_locations,
                    'form_hours': form_hours,
                    'error_vr': error_vr
                })
        return redirect('AdminLocations')
    
    def show(self, request, id):
        location = Location.objects.get(id=id)
        opening_hours = OpeningHour.objects.filter(location=location)
        
        return render(request, 'AdminLocationsInfo.html', {
            'location': location,
            'opening_hours': opening_hours,
        })
        
    def update(self, request, id):
        location = Location.objects.get(id=id)
        opening_hours = OpeningHour.objects.filter(location=location)

        OpeningHoursFormSet = modelformset_factory(OpeningHour, extra=0, form=OpeningHoursForm)

        if request.method == 'POST':
            location_form = LocationsForm(request.POST, instance=location)
            formset = OpeningHoursFormSet(request.POST, queryset=opening_hours)

            if location_form.is_valid() and formset.is_valid():
                location = location_form.save()

                for form in formset:
                    opening_hour = form.save(commit=False)
                    opening_hour.location = location
                    opening_hour.save()

                return redirect('AdminLocations')  # Redirigir a la página de éxito

        else:
            location_form = LocationsForm(instance=location)
            formset = OpeningHoursFormSet(queryset=opening_hours)

        return render(request, 'AdminLocationsEdit.html', {
            'form_location': location_form,
            'form_hours': formset,
            'location': location,
        })
    
    def delete(self, request, id):
        location = Location.objects.get(id=id)
        location.delete()
        return redirect('AdminLocations')