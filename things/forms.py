"""Forms of the project."""
from django import forms
from django.core import validators


class ThingForm(forms.Form):
    name = forms.CharField(max_length=36, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    quantity = forms.IntegerField(widget=forms.NumberInput, min_value=0, max_value=50)
