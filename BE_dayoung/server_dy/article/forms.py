from django import forms


class SearchForm(forms):
    word = forms.Charfield(label='Search Word')
