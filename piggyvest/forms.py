from django import forms
"""
Choices = (("cs", "Piggybank CoreSavings"),
           ("tl", "Target lock"), ("flex", "Flex"), ("flex dollar", "Flex Dollar"))


class Plansform(forms.Form):
    choice = forms.ChoiceField(Choices)

"""
class Interestform(forms.Form):
    capital = forms.IntegerField(label="capital")
    time = forms.IntegerField(label="saving time in years")
