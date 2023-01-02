from django.shortcuts import render
from .models import User
from myapp.forms import StudentRegistration
from django.views.generic.base import View,TemplateView,RedirectView
# Create your views here.
class UserAddProfile(TemplateView):
    template_name = 'myapp/addshow.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu':stud,'form':fm}
        return context

