from client.imports import *


def logout_view(request):
    logout(request)
    return redirect(reverse('client:login'))