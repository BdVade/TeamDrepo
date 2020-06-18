from django.shortcuts import render
from django.http import HttpResponse
from .forms import Interestform

"""Plansform"""
from django.views.generic import View

"""
class Plan(View):
    def get(self, request):
        params = {}
        form = Plansform()
        params["form"] = form
        return render(request, 'index.html', params)

    def post (self,request):
        form = Plansform(request.POST)
        params = {}
        if form.is_valid():
            if form.cleaned_data["choice"] =="Piggybank CoreSavings":
                rate = 0.1
            elif form.cleaned_data["choice"] =="Target lock":
                rate = 0.1
            elif form.cleaned_data["choice"] =="Flex":
                rate = 0.1
            elif form.cleaned_data["choice"] =="Flex Dollar":
                rate = 0.06
"""


class InterestCalc(View):
    def get(self, request):
        params = {}
        form = Interestform()
        params["form"] = form
        return render(request, 'index.html', params)

    def post(self, request):
        form = Interestform(request.POST)
        params = {}
        if form.is_valid():
            capital = form.cleaned_data["capital"]
            time = form.cleaned_data["time"]
            if form.cleaned_data["choice"] == "Piggybank CoreSavings":
                rate = 0.1
            elif form.cleaned_data["choice"] == "Target lock":
                rate = 0.1
            elif form.cleaned_data["choice"] == "Flex":
                rate = 0.1
            elif form.cleaned_data["choice"] == "Flex Dollar":
                rate = 0.06
            interest = (capital * time * rate)
            total = interest + capital
            params["interest"] = interest
            params["total"] = total
        else:
            return HttpResponse("form filled incorrectly go back to refill" + form.errors)
        return render(request, "interest.html", params)
