from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('addnft',views.addnft, name='addnft'),
    path('contact',views.contact, name='contact'),
    path('events',views.events, name='events'),
    
]