from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import models, form

# Create your views here.
# class ThemesView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'AdminThemes.html')
class ThemesView(LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        formulario = form.ThemeForm()
        temas = models.Theme.objects.all()
        return render(request, 'AdminThemes.html', {
            'form': formulario, 
            'themes': temas, 
            })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            temas = models.Theme.objects.all()
            formulario = form.ThemeForm(request.POST, request.FILES or None)
            if formulario.is_valid():
                formulario.save()
            else:
                error_vr = "El formulario no es valido"
                return render(request, 'AdminThemes.html', {
                    'form': formulario, 
                    'themes': temas,
                    'error_vr': error_vr,
                })
        return redirect('AdminThemes')
    
    def show(self, request, id, **kwargs):
        theme = models.Theme.objects.get(id=id)
        return render(request, 'AdminThemesInfo.html',{
            'theme': theme,
        })
    
    def update(self, request, id, **kwargs):
        theme = models.Theme.objects.get(id=id)
    
        if request.method == 'POST':
            service_form = form.ThemeForm(request.POST, instance=theme)
    
            if service_form.is_valid():
                service_form.save()  # Guardar los cambios en el formulario
                return redirect('AdminThemes')  # Redirigir a la página de éxito
        else:
            service_form = form.ThemeForm(instance=theme)
    
        return render(request, 'AdminThemesEdit.html', {
            'theme': theme,
            'form': service_form
        })
    
    def delete(self, request, id):
       location = models.Theme.objects.get(id=id)
       location.delete()
       return redirect('AdminThemes')