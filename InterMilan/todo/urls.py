from .imports import *
from .views.client_tasks import client_tasks

app_name = 'todo'

urlpatterns = [

    path('task/',tasks_manager, name='tasks'),
    path('mmd/<int:id>',client_tasks,name = 'client_tasks')

]