from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    # def get_absolute_url(self):
    #     return reverse("thankyu")
    def get_absolute_url(self):
        return reverse("studentdetails", kwargs={"pk": self.pk})
    