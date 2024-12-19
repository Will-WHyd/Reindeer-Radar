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
    # Get households belonging to the logged-in user
    household_list = Household.objects.filter(user=request.user)
    
    # Filter kids only for households that are marked as not visited
    visited_households = Household.objects.filter(user=request.user, visited=False)
    naughty_count = Kid.objects.filter(family__in=visited_households, behavior='Naughty').count()
    nice_count = Kid.objects.filter(family__in=visited_households, behavior='Nice').count()

    context = {
        "household_list": household_list,
        "naughty_count": naughty_count,
        "nice_count": nice_count,
    }
    return render(request, 'journey/list.html', context)



def add_house(request):
    """ 
    Creates a new instance of Household via form
    """ 
    h_form = HouseholdForm()
    
    if request.method == 'POST':
        h_form = HouseholdForm(request.POST)
        if h_form.is_valid():
            household = h_form.save(commit=False)
            household.user = request.user
            household.save()

            messages.add_message(
                request, messages.SUCCESS,
                'New Destination Added! Christmas Joy inbound!'
            )

            return redirect('journey')

    return render(request, 'journey/add_house.html', {'h_form': h_form})

def add_kid(request, id):
    """ 
    Creates a new instance of Kid via form and associates it with a household
    """ 
    household = get_object_or_404(Household, id=id)
    k_form = KidForm()

    if request.method == 'POST':
        k_form = KidForm(request.POST)
        if k_form.is_valid():
            kid = k_form.save(commit=False)
            kid.user = request.user
            kid.family = household
            kid.save()

            messages.add_message(
                request, messages.SUCCESS,
                f'New Kid Added to the { household.name } house! Christmas Joy inbound!'
            )

            return redirect('journey')

    return render(request, 'journey/add_kid.html', {'k_form': k_form})
