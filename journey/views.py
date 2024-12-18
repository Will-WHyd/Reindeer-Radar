from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Household, Kid


# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'journey/index.html'


def journey_list(request):

    households = Household.objects.all()

    return render(request, 'journey/list.html', {"households": households})
