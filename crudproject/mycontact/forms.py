from django import forms
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','email','password']
        widgets = {'name':forms.TextInput(attrs={'class':'myform'}),
            'password':forms.PasswordInput(attrs={'class':'mypass'})
        } 