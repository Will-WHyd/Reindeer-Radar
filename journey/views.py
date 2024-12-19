from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
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

@login_required
def edit_house(request, id):
    household = get_object_or_404(Household, id=id) 
    h_form = HouseholdForm()

    if request.method == 'POST':
        h_form = HouseholdForm(request.POST, instance=household)
        if h_form.is_valid():
            h_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New Destination Added! Christmas Joy inbound!'
            )

            return redirect('journey')
    else:
        h_form = HouseholdForm(instance=household)

    return render(request, 'journey/add_house.html', {'h_form': h_form, 'household': household})


def delete_house(request, id):
    household = get_object_or_404(Household, id=id) 
    if household.user == request.user:
        household.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Appointment Deleted!'
            )
        return redirect('journey')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You do not have permission!'
            )
        return redirect('journey')


@login_required
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


@login_required
def edit_kid(request, id):
    kid = get_object_or_404(Kid, id=id) 
    k_form = KidForm()

    if request.method == 'POST':
        k_form = KidForm(request.POST, instance=kid)
        if k_form.is_valid():
            k_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Kid's details updated!"
            )

            return redirect('journey')
    else:
        k_form = KidForm(instance=kid)

    return render(request, 'journey/add_kid.html', {'k_form': k_form, 'kid': kid})


def delete_kid(request, id):
    kid = get_object_or_404(Kid, id=id) 
    if kid.user == request.user:
        kid.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Kid removed from the list'
            )
        return redirect('journey')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You do not have permission!'
            )
        return redirect('journey')


@csrf_exempt
def update_visited(request):
    if request.method == "POST":
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            household_id = data.get("household_id")
            visited_status = data.get("visited")

            # Validate input
            if household_id is None or visited_status is None:
                return JsonResponse({"success": False, "message": "Invalid data provided."}, status=400)

            household = Household.objects.get(id=household_id, user=request.user)
            household.visited = visited_status
            household.save()

            # Recalculate counts for nice and naughty kids
            visited_households = Household.objects.filter(user=request.user, visited=False)
            naughty_count = Kid.objects.filter(family__in=visited_households, behavior='Naughty').count()
            nice_count = Kid.objects.filter(family__in=visited_households, behavior='Nice').count()

            return JsonResponse({"success": True, "nice_count": nice_count, "naughty_count": naughty_count})

        except Household.DoesNotExist:
            return JsonResponse({"success": False, "message": "Household not found."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)