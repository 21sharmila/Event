from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('event/add/', views.add_event, name='add_event'),
    path('event/<int:pk>/edit/', views.update_event, name='update_event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete_event'),
]

