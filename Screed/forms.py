from django import forms
from .models import Choice, Node, Check, Reward, ItemDefinition

class NewChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

class NewNodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['title', 'text']

class NewItemForm(forms.ModelForm):
    class Meta:
        model = ItemDefinition
        fields = ['name', 'type', 'description', 'quantity', 'power_type', 'power', 'cost_type', 'cost']

class NewRewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['item']

class NewCheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['title', 'success_message', 'failure_message', 'stat_type', 'value', 'item_requirement']