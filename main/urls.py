from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('team', views.team, name="team"),
    path('gallary',views.images, name="images"),
    path('events', views.events, name="events"),
    path('contact', views.contact, name="contact"),
    path('resources', views.resources, name="resources")
]