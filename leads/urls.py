from django.urls import path
from . import views

urlpatterns = [
    path('',             views.index,       name='index'),
    path('api/leads',    views.create_lead, name='create_lead'),
    path('api/leads/',   views.list_leads,  name='list_leads'),
]
