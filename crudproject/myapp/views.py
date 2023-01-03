from django.shortcuts import render,HttpResponseRedirect
from .models import User
from myapp.forms import StudentRegistration
from django.views.generic.base import View,TemplateView,RedirectView
from django.views.generic.list import ListView
from .views import View
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

class StudentListView(ListView):
    model = User
    



class UserDelete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        myid = kwargs['id']
        data = User.objects.get(id = myid)
        data.delete()
        return super().get_redirect_url(*args, **kwargs)

class UserUpdateView(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request,'myapp/update.html',{'form':fm})

    def post(self, request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'myapp/update.html',{'form':fm})
