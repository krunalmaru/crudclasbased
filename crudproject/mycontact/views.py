from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import ContactForm, StudentForm
from django import forms
from django.views.generic.base import TemplateView,View,RedirectView,TemplateResponseMixin
from django.views.generic.edit import FormView,CreateView,UpdateView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import BaseUpdateView
from .models import Student
# Create your views here.

class ContactFormView(FormView):
    template_name = 'mycontact/contact.html'
    form_class = ContactForm
    success_url = '/thankyu/'
    initial = {'name':'your Name','email':'rahul@gmail.com','message':'your Message'}
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['message'])
        # return super().form_valid(form)
        return HttpResponse('msg sent')

class ThankyuTemplatesView(TemplateView):
    template_name = 'mycontact/thankyu.html'
     
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['id','name','email','password']
#     # success_url = '/thankyu/'
#     template_name = 'mycontact/studentform.html'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'myform'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
#         return form

    ''''studentmodelform use'''
class StudentCreateView(CreateView):
    form_class = StudentForm
    # fields = ['id','name','email','password']
    # success_url = '/thankyu/'
    template_name = 'mycontact/studentform.html'

class StudentDetailView(DetailView):
    model = Student

# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['id','name','email','password']
#     success_url = '/thankyu/'
#     template_name = 'mycontact/studentform.html'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    # fields = ['id','name','email','password']
    success_url = '/thankupdate/'
    template_name = 'mycontact/studentform.html'

class ThankTemplatsView(TemplateView):
    template_name = 'mycontact/thanksupdate.html'
