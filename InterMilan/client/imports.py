from django.shortcuts import render , redirect
from  django.contrib.auth.models import User
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

from .views.home import home
from .views.login_view import login_view
from .views.logout import logout_view
from .views.register import register
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .views.edit_profile import  edit_profile
from client import views
from django.contrib.auth.decorators import login_required, user_passes_test