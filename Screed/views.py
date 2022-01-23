from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Screed.models import *
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'index.html', {})


