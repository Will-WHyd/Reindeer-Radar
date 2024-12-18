from . import views
from django.urls import path


urlpatterns = [
    path('add_house/', views.add_house, name='add_house'),
    path('<id>/add_kid/', views.add_kid, name='add_kid'),
    path('journey/', views.journey_list, name='journey'),
    path('', views.HomePage.as_view(), name='home'),
]