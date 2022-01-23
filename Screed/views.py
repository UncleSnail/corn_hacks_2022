from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Screed.models import *

def index(request):
    paragraphs = ['Does this work?','Am I sciencing?']
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'index.html',context)


@login_required
def private_place(request):
    return HttpResponse("Don't have access!", content_type="text/plain")
