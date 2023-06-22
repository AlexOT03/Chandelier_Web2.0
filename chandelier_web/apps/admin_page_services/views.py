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
        
    def show(self, request, id, **kwargs):
        service = models.Service.objects.get(id=id)
        return render(request, 'AdminServicesInfo.html', {
            'service': service
        })
    
    def update(self, request, id, **kwargs):
        service = models.Service.objects.get(id=id)
    
        if request.method == 'POST':
            service_form = form.ServicesForm(request.POST, instance=service)
    
            if service_form.is_valid():
                service_form.save()  # Guardar los cambios en el formulario
                return redirect('AdminServices')  # Redirigir a la página de éxito
    
        else:
            service_form = form.ServicesForm(instance=service)
    
        return render(request, 'AdminServicesEdit.html', {
            'service': service,
            'form': service_form
        })

    
    def delete(self, request, id):
       service = models.Service.objects.get(id=id)
       service.delete()
       return redirect('AdminServices')