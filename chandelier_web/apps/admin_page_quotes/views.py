from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
class QuotesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'AdminQuotes.html')