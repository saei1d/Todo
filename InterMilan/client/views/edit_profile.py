from client.imports import *
from client.models import CustomUser


@login_required
def edit_profile(request):
    if request.method == 'POST':
        # username = request.POST.get('username_new')
        firstname = request.POST.get('firstname')
        lastname  = request.POST.get('lastname')
        cellphone = request.POST.get('cellphone')
        user = CustomUser.objects.get(id=request.user.id)
        user.first_name = firstname
        user.last_name = lastname
        user.cellphone = cellphone
        user.save()
        return redirect(reverse('client:home'))


    else:
        return render(request, 'edit_profile.html')