from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def user_redirect(request):
    return HttpResponseRedirect(reverse(user, args=[request.user.id]))

# @login_required
def traveler(request, traveler_id):
    traveler = get_object_or_404(Traveler, pk=traveler_id)
    context = {'traveler': traveler}
    return render(request, 'traveler.html', context)

def choice(request, traveler_id, choice_id):
    # Get the traveler and the choice.
    traveler = get_object_or_404(Traveler, pk=traveler_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    context = {
        'traveler': traveler,
        'choice': choice
    }
    # Update the traveler based on the choice.
    traveler.node = choice.target
    traveler.save()

    # Display the new traveler page.
    return render(request, 'traveler.html', context)

# def new(request, user_id, parent_id):
    # user = get_object_or_404(User, pk=user_id)
    # parent = get_object_or_404(Node, pk=parent_id)
    # context = {
    #     'user': user,
    #     'parent': parent
    # }
#     return render(request, 'new.html', context)

from .forms import NewForm

def new_node(request, user_id, parent_id):
    user = get_object_or_404(User, pk=user_id)
    parent = get_object_or_404(Node, pk=parent_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewForm()

    context = {
        'user': user,
        'parent': parent,
        'form': form
    }
    return render(request, 'new.html', context)