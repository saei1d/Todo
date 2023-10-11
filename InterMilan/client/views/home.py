from ..imports import *
from todo.models import Task
from ..models import CustomUser


@login_required
def home(request):
    context={}

    if request.user.is_superuser:
        context['users'] = CustomUser.objects.filter()







    if request.method=='POST':

        title = request.POST.get('input')

        task = Task()
        task.title = title
        task.username = request.user
        task.save()
    context['mmd'] = Task.objects.filter(username=request.user).order_by('-id')[:4]










    # Task.objects.filter(some_field=).delete()

    return render(request, 'home.html', context)



