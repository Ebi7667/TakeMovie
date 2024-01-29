from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
class UserRegistareView(CreateView):
    form_class=UserCreationForm
    template_name='registration/registre.html'
    success_url=reverse_lazy('login')
