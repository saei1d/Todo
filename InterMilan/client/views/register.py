from client.models import *
from ..imports import *
import re


def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if CustomUser.objects.filter(username=username).exists():
            context['error'] = True
            context['error_msg'] = 'Username has exist!!!'
        else:
            user = CustomUser(username=username)
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if re.fullmatch(regex, email):
                user.email = email
                user.set_password(password)
                user.save()
                return redirect(reverse('client:login'))
            else:
                context['error_msg'] = "email is invalid!!!!"
    return render(request, 'register.html', context)
