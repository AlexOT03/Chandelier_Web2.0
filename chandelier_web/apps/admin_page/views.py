from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import View
from chandelier_web.apps.admin_page_locations.models import Location
from chandelier_web.apps.home_page.models import Message
# from django.core.mail import send_mail

# Create your views here.
class AdminIndex(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        location = Location.objects.all()
        messages = Message.objects.all()
        return render(request, 'AdminIndex.html', {
            'location': location,
            'messages': messages,
        })
    
    def logoutCrud(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
    
class AdminMessages(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        return render(request, 'AdminMessage.html', {
            'messages': messages,
        })
    
    def show(self, request, id, **kwargs):
        message = Message.objects.get(id=id)
        return render(request, 'AdminMessageInfo.html', {
            'message': message,
        })
        
    def delete(self, request, id, **kwargs):
        message = Message.objects.get(id=id)
        message.delete()
        return redirect('AdminMessages')