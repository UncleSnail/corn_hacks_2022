from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Screed.models import *


def index(request):
    return render(request, 'index.html', {})

@login_required
def private_place(request):
    return HttpResponse("Don't have access!", content_type="text/plain")