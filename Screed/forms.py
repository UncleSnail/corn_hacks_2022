from django import forms

class NewForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
