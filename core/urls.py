from django.urls import path
from .views import viewindex

urlpatterns = [
    path('',viewindex, name='index_page' ),
] 
