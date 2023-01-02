from django import forms


class EmailForm(forms.Form):
    message = forms.CharField()