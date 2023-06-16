from django.shortcuts import render
from django.views import View
from chandelier_web.apps.admin_page_locations.models import Location
from chandelier_web.apps.admin_page_states.models import State
from chandelier_web.apps.admin_page_themes.models import Theme

# Create your views here.
class indexHome(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        estados = State.objects.all()
        temas = Theme.objects.all()
        return render(request, 'index.html', {
            'locations': locations, 
            'estados': estados, 
            'temas': temas
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
                places = Location.objects.filter(state_id=id)
            else:
                dato = Theme.objects.get(id=id)
                places = Location.objects.filter(theme_id=id)
        new_reference = reference
        return render(request, 'location.html',{
            'temas':temas,
            'new_reference':new_reference,
            'dato':dato,
            'places':places,
        })

class locationInfoHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'locationInfo.html')
    
class aboutUsHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
    
class contactHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contactUs.html')