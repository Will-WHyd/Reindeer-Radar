from . import views
from django.urls import path

app_name = 'journey'

urlpatterns = [
    path('add_house/', views.add_house, name='add'),
    path('journey/', views.journey_list, name='journey'),
    path('', views.HomePage.as_view(), name='home'),
]