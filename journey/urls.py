from . import views
from django.urls import path


urlpatterns = [
    path('add_house/', views.add_house, name='add_house'),
    path('edit_house/<id>', views.edit_house, name='edit_house'),
    path('delete_house/<id>', views.delete_house, name='delete_house'),
    path('<id>/add_kid/', views.add_kid, name='add_kid'),
    path('edit_kid/<id>', views.edit_kid, name='edit_kid'),
    path('delete_kid/<id>', views.delete_kid, name='delete_kid'),
    path('journey/', views.journey_list, name='journey'),
    path('update-visited/', views.update_visited, name='update_visited'),
    path('', views.HomePage.as_view(), name='home'),
]