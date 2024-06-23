from core.models import Task, TaskStatus, InProgressTask, TodoTask, CompletedTask

# pip install django-extensions
# ./manage.py runscript proxy_models
# ./manage.py shell_plus --print-sql


def run():
    """ 
        it is ->>>        < in_progress = InProgressTask.objects.all() >
        instead of ->>>   < in_progress = Task.objects.filter(status = TaskStatus.IN_PROGRESS) >
    """
    
    # in_progress = InProgressTask.objects.all()
    # print(in_progress)
    
    # todo = TodoTask.objects.all()
    # print(todo)
    
    # completed = CompletedTask.objects.all()
    # print(completed)

    """
        Overridden save() method gives us not to write 'status=...' 
        
        get_status_display() ->>>  get_< field name >_display() - to see human readable representation
    """
    # task = InProgressTask.objects.create(name="Learn Math")
    # print(task)
    # print(task.get_status_display())

    print(CompletedTask.objects.all())
