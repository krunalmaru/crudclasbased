from django.shortcuts import render,HttpResponseRedirect
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
    
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

class UserDelete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        myid = kwargs['id']
        data = User.objects.get(id = myid)
        data.delete()
        return super().get_redirect_url(*args, **kwargs)

