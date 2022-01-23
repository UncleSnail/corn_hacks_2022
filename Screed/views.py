from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Screed.models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import NewChoiceForm, NewNodeForm

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

def new(request, user_id, parent_id):
    user = get_object_or_404(User, pk=user_id)
    parent = get_object_or_404(Node, pk=parent_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        node_form = NewNodeForm(request.POST)
        choice_form = NewChoiceForm(request.POST)
        # check whether it's valid:
        if choice_form.is_valid() and node_form.is_valid():
            # process the data in form.cleaned_data as required
            new_node = Node(
                title = node_form.cleaned_data['title'],
                text = node_form.cleaned_data['text']
            )
            new_node.save()
            new_node.authors.add(user)
            # Choice
            new_choice = Choice(
                text = choice_form.cleaned_data['text'],
                parent = parent,
                target = new_node
            )
            new_choice.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        choice_form = NewChoiceForm()
        node_form = NewNodeForm()

    context = {
        'user': user,
        'parent': parent,
        'choice_form': choice_form,
        'node_form': node_form
    }
    return render(request, 'new.html', context)