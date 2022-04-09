from django import forms


class TownForm(forms.Form):
    town = forms.CharField(
        max_length=200,
        )
