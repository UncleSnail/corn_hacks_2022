from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    paragraphs = ['Does this work?','Am I sciencing?']
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'index.html',context)