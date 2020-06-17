from django import forms


class Interestform(forms.Form):
    capital = forms.IntegerField()
    time = forms.IntegerField()