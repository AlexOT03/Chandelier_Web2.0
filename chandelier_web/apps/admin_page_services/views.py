from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import models, form

# Create your views here.
class ServicesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        formulario = form.ServicesForm()
        servicios = models.Service.objects.all()
        return render(request, 'AdminServices.html', {
            'form': formulario,
            'services': servicios,
        })
        
    def post(self, request, *args, **kwargs):
        servicios = models.Service.objects.all()
        if request.method == 'POST':
            formulario = form.ServicesForm(request.POST)
            if formulario.is_valid():
                print('successfully')
                formulario.save()
                return redirect('AdminServices')  # Redirige a la página de servicios o donde desees
        else:
            formulario = form.ServicesForm()
        return render(request, 'AdminServices.html', {
            'form': formulario,
            'services': servicios,
            })