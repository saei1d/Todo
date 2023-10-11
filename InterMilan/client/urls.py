from .imports import *

app_name = 'client'



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('edit/',edit_profile, name='edit_profile'),
    path('logout/',logout_view,name= 'logout'),

]
