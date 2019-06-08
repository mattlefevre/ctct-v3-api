from django.shortcuts import render,redirect, reverse
from django.views.generic import FormView, TemplateView
import logging
import requests as r
import os

# local packages
from v3API.forms import SignUpForm
from v3API.services import get_authorization, get_tokens


class ConnectCTCTView(TemplateView):
    http_method_names = ["get", "post"]
    template_name = "connectctct.html"
    
    def get_context_data(self, **kwargs):
        context = super(ConnectCTCT, self).get_context_data(**kwargs)
        context['code'] = self.request.GET.get('code',False)
        request = get_tokens(context['code'])
        context['token'] = request.json
        return context
    
    def post(self, request):
        return redirect(get_authorization())

class SignUpView(FormView):
    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = '/success/'
        
    def form_valid(self, form):
        # NOTE: Send form data to CTCT
        return super().form_valid(form)

    
class SuccessView(TemplateView):
    template_name = "success.html"
