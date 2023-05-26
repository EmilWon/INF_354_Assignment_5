from django.db import models
# from django.forms import ModelForm, fields

# Create your models here.

class Appointments(models.Model):
    studentNum = models.CharField(max_length=9)
    studentName = models.CharField(max_length=100)
    appointDate = models.DateTimeField(blank=True, null=True)
    appointDesc = models.CharField(max_length=250)

    def __str__(self):
        return self.studentName

# class AppointForm(ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['studentNum','studentName','appointDate','appointDesc']

