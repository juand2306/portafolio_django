from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from datetime import datetime, timedelta
# from .forms import 
# from .models import 
from django.http import HttpResponseServerError
# Create your views here.

def viewindex (request):
    return render (request, 'index2.html')