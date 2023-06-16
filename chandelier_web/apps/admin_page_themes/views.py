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
            formulario = form.ThemeForm(request.POST, request.FILES)
            if formulario.is_valid():
                print('success')
                formulario.save()
            else:
                print('Invalid')
                formulario = form.ThemeForm()
        return redirect('AdminThemes')