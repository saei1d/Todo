from todo.imports import *
from todo.models import Task


def client_tasks(request,id):
    if request.user.is_superuser:
        context ={}
        context['mmdjavad'] = Task.objects.filter(username=id)


        return render(request,'tasks.html',context)

    return redirect(reverse('client:home'))









