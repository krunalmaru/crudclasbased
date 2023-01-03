from django.shortcuts import render,HttpResponseRedirect
from .models import User
from myapp.forms import StudentRegistration
from django.views.generic.base import View,TemplateView,RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
            
class StudentDetailView(DetailView):
    model = User
    template_name = 'myapp/user.html'

class StudentListView(ListView):
    model = User
    # template_name_suffix = '_get'
    # ordering = 'password'
    # template_name = 'myapp/user.html'
    # context_object_name = 'user'

    
'''############### list view method  ############'''
    # def get_queryset(self):
    #     return User.objects.filter(name__icontains='L')
    
    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['obj'] = User.objects.all().order_by('name')
    #     return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'abhy':
    #         template_name = 'myapp/abhy.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

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
