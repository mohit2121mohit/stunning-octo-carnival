from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name= 'home'),
    path('live-train-status', views.livetrainstatus, name='livetrainstatus'),
    path("train-between-stations", views.trainbetweenstations, name= 'trainbetweenstations'),
    path("pnr-status", views.pnrstatus, name= 'pnrstatus'),
    path("train-by-station", views.trainbystation, name= 'trainbystation'),
    path("train-schedule", views.trainschedule, name= 'trainschedule'),
    path("heritage-trains", views.heritagetrains, name= 'heritagetrains'),
    
]
