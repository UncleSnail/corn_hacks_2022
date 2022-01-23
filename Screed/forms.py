from django import forms
from .models import Choice, Node

class NewChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

class NewNodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['title', 'text']