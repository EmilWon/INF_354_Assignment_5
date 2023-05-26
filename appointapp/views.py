from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .models import Appointments
import os
from django.http import HttpResponse
from django.http.response import Http404

# from .forms import AppointForm

# def index(request):
#     if request.method == 'POST':
#         form = AppointForm(request.POST)

#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')

#     else:
#         form = AppointForm()

#     return render(request, 'index.html', {'form': form})

# Create your views here.

def display(request):
    app = Appointments.objects.all()
    return render(request, "index.html", {'file': app})