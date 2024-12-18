from . import views
from django.urls import path


urlpatterns = [
    path('journey/', views.journey_list, name='journey'),
    path('', views.HomePage.as_view(), name='home'),
]