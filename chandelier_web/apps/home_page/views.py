from django.shortcuts import render, redirect
from django.views import View
from chandelier_web.apps.admin_page_locations.models import Location, OpeningHour
from chandelier_web.apps.admin_page_states.models import State
from chandelier_web.apps.admin_page_themes.models import Theme
from chandelier_web.apps.home_page.models import Message
from chandelier_web.apps.home_page.form import MessageForm

# Create your views here.
class indexHome(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        estados = State.objects.all()
        return render(request, 'index.html', {
            'locations': locations, 
            'estados': estados,
            })
    
class fastQuoteHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fastQuote.html')
    
class quoteHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quote.html')
    
class locationHome(View):
    def get(self, request ,reference, id):
        temas = Theme.objects.all()
        dato = None
        places = None
        if reference != "all":
            if reference == "estado":
                dato = State.objects.get(id=id)
                places = Location.objects.filter(state=id)
            else:
                dato = Theme.objects.get(id=id)
                places = Location.objects.filter(theme=id)
        else:
            places = Location.objects.all()
        new_reference = reference
        return render(request, 'location.html',{
            'temas':temas,
            'new_reference':new_reference,
            'dato':dato,
            'locations':places,
        })

class locationInfoHome(View):
    def get(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        opening_hours = OpeningHour.objects.filter(location=location)
        
        return render(request, 'locationInfo.html', {
            'location': location,
            'opening_hours': opening_hours,
        })
    
class aboutUsHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
    
class contactHome(View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        
        return render(request, 'contactUs.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'contactUs.html', {
                'form': form,
            })
        return redirect('contactHome')
