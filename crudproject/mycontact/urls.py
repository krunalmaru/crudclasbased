from django.urls import path
from mycontact import views

urlpatterns = [
    path('contact', views.ContactFormView.as_view(),name='contact'),
    path('thankyu/',views.ThankyuTemplatesView.as_view(),name='thankyu'),
    path('students/',views.StudentCreateView.as_view(),name='students'),
    path('update/<int:pk>',views.StudentUpdateView.as_view(),name='updatestudent'),
    path('thankupdate/', views.ThankUpdateTemplatsView.as_view(),name='thanksupdate'),
    path('delete/<int:pk>',views.StudentDeleteView.as_view(),name='deletestudent'),
    path('thanksdelete/',views.ThankDeleteTemplateView.as_view(),name='thanksdelete')

]
