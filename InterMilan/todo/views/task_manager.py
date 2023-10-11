from todo.imports import *
from todo.models import Task


# Create your views here.


def tasks_manager(request):
    context = {}
    if request.method=='POST':
        title = request.POST.get('input')
        task = Task()
        task.title = title
        task.username = request.user
        task.save()
    elif request.method == 'GET':
        try:
            if 'delete' in request.GET:
                t = Task.objects.get(id=request.GET.get('delete'), username=request.user)
                t.delete()
                context['msg'] = 'delete done!'
                return redirect(reverse('todo:tasks'))
            if 'check' in request.GET:
                t = Task.objects.get(id=request.GET.get('check'), username=request.user)
                t.checked()
                context['msg'] = 'check done!'
                return redirect(reverse('todo:tasks'))
            else:
                t = Task.objects.get(id=request.GET.get('uncheck'), username=request.user)
                t.unchecked()
                context['msg'] = 'uncheck done!'
                return redirect(reverse('todo:tasks'))


        except:
            pass
    context['mmd'] = Task.objects.filter(username=request.user).order_by('-id')
    return render(request, 'tasks.html', context)






