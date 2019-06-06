from django.shortcuts import render
from django.views.generic import FormView
from .forms import SignUpForm

# Create your views here.

class SignUpView(FormView):
    form_class = SignUpForm
    success_url = '/success/'

    def form_valid(self, form):
        # Sends contact to CTCT
        return super().form_valid(form)