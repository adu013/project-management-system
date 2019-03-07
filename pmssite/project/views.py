from django.views.generic import DetailView, ListView
from .models import Project, Task


class IndexView(ListView):
    model = Project
    context_object_name = 'project_list'
    queryset = Project.objects.all()
    template_name = 'project/index.html'


class DetailView(DetailView):
    model = Task
    slug_field = 'project_id'
    slug_url_kwargs = 'project_id'
    context_object_name = 'task_list'
    template_name = 'project/detail.html'

    def get_queryset(self):
        return Task.objects.filter(pk=project_id)

class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task_detail'
    queryset = Task.objects.all()
    template_name = 'project/task.html'
