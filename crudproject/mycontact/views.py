from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.base import TemplateView,View,RedirectView
from django.views.generic.edit import FormView 
# Create your views here.

class ContactFormView(FormView):
    template_name = 'mycontact/contact.html'
    form_class = ContactForm
    success_url = '/thankyu/'

class ThankyuTemplatesView(TemplateView):
    template_name = 'mycontact/thankyu.html'
     
