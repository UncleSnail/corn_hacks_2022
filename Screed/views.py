from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Screed.models import *
from django.contrib.auth.forms import UserCreationForm


def index(request):
    paragraphs = ['Does this work?','Am I sciencing?']
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'index.html', context)

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'user.html', context)

def traveler(request, traveler_id):
    traveler = get_object_or_404(Traveler, pk=traveler_id)
    context = {'traveler': traveler}
    return render(request, 'traveler.html', context)
