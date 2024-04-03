# forms.py

from django import forms

class InputForm(forms.Form):
    input_text = forms.CharField(label='Input Text')

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

