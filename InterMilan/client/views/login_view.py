from client.imports import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('client:home'))
    return render(request, 'logi
    
    
    
    
    
    
    
    
    
    
    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyNTE0MDIwLCJpYXQiOjE2OTI0Mjc2MjAsImp0aSI6IjRkMDljMWNmMmVkMjQxZDZiODQ4N2ExNGJlODk5ZWM1IiwidXNlcl9pZCI6Mn0.iZg-iLEUOi15GvkdKim7Zn7tO35i2ZXIF_nmoM-4pMo
