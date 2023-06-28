from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import form, models

# Create your views here.
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
            estados = models.State.objects.all()
            formulario = form.StateForm(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
            else:
                error_vr = "El formulario no es válido"
                return render(request, 'AdminStates.html', {
                    'form': formulario,
                    'error_vr': error_vr,
                    'states':estados, 
                })
        return redirect('AdminStates')
    
    def show(self, request, id, **kwargs):
        state = models.State.objects.get(id=id)
        return render(request, 'AdminStatesInfo.html', {
            'state': state
        })
    
    def update(self, request, id, **kwargs):
        state = models.State.objects.get(id=id)
        
        if request.method == 'POST':
            state_form = form.StateForm(request.POST, request.FILES, instance=state)
            
            if state_form.is_valid():
                state_form.save()
                return redirect('AdminStates')
        
        else:
            state_form = form.StateForm(instance=state)
            
        return render(request, 'AdminStatesEdit.html', {
            'state': state,
            'form': state_form,
        })
    
    def delete(self, request, id):
       state = models.State.objects.get(id=id)
       state.delete()
       return redirect('AdminStates')