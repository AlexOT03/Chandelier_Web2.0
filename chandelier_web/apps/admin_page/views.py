from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import View
from chandelier_web.apps.admin_page_locations.models import Location
# from django.core.mail import send_mail

# Create your views here.
class AdminIndex(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        location = Location.objects.all()
        return render(request, 'AdminIndex.html', {
            'location': location,
        })
    
    def logoutCrud(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
    
class AdminMessages(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'AdminMessage.html')