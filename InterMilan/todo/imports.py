from django.shortcuts import render, redirect
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import HttpResponse
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import path
from .views.task_manager import tasks_manager
