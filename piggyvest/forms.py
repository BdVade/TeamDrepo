from django import forms

Choices = (("Piggybank CoreSavings","Piggybank CoreSavings"),
           ("Target lock","Target lock"), ("Flex","Flex"), ("Flex Dollar","Flex Dollar"),)


class Interestform(forms.Form):

    capital = forms.IntegerField(label="capital")
    time = forms.IntegerField(label="saving time in years")
    choice = forms.ChoiceField(choices=Choices)