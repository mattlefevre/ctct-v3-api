from django.shortcuts import render,redirect, reverse
from django.views.generic import FormView, TemplateView
import logging
import requests as r
import os

# local packages
from v3API.forms import SignUpForm
from v3API.services import CTCTAuth, CTCTContactAPIs


class ConnectCTCTView(TemplateView):
    http_method_names = ["get", "post"]
    template_name = "connectctct.html"
    
    def get_context_data(self, **kwargs):
        context = super(ConnectCTCTView, self).get_context_data(**kwargs)
        context['code'] = self.request.GET.get('code',False)
        request = CTCTAuth.get_tokens(context['code'])
        context['token'] = request.json
        return context
    
    def post(self, request):
        return redirect(CTCTAuth.get_authorization())

class SignUpView(FormView):
    http_method_names = ["get", "post"]
    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = 'success'
        
    def form_valid(self, form):
        first_name = form['first_name']
        email_address = form['email']

        request = CTCTContactAPIs.add_contact(first_name, email_address)
        print(request)
        return redirect('success')

    
class SuccessView(TemplateView):
    template_name = "success.html"
