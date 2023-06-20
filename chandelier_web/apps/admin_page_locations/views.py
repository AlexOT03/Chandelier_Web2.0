from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from .models import Location
from .form import LocationsForm, OpeningHoursForm

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
                return HttpResponse('<script>alert("El formulario no es válido"); window.location.href="/admin/ubicaciones/";</script>')
        return redirect('AdminLocations')