from django.urls import path
from mycontact import views

urlpatterns = [
    path('contact', views.ContactFormView.as_view(),name='contact'),

]
