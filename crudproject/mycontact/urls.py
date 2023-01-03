from django.urls import path
from mycontact import views

urlpatterns = [
    path('contact', views.ContactFormView.as_view(),name='contact'),
    path('thankyu/',views.ThankyuTemplatesView.as_view(),name='thankyu'),

]
