from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import form, models

# Create your views here.
# class StatesView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'AdminStates.html')
class StatesView(LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        formulario = form.StateForm()
        estados = models.State.objects.all()
        return render(request, 'AdminStates.html', {
            'form': formulario,
            'states':estados, 
            })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            formulario = form.StateForm(request.POST, request.FILES)
            if formulario.is_valid():
                print('success')
                formulario.save()
            else:
                print('Invalid')
                formulario = form.StateForm()
        return redirect('AdminStates')