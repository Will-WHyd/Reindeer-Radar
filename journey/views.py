from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Household, Kid
from .forms import *


# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'journey/index.html'


def journey_list(request):

    household_list = Household.objects.all()


    return render(request, 'journey/list.html', {"household_list": household_list})


def add_house(request):
    """ 
    Creates a new instance of Household via form
    """ 
    h_form = HouseholdForm()
    
    if request.method == 'POST':
        h_form = HouseholdForm(request.POST)
        if form.is_valid():
            household = h_form.save(commit=False)
            household.user = request.user
            household.save()

            messages.add_message(
                request, messages.SUCCESS,
                'New Destination Added! Christmas Joy inbound!'
            )

            return redirect('journey/list.html')
        return render(request, 'journey/add_house.html', {'h_form': h_form})
