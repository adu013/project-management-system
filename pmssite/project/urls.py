from django.urls import path
from .views import IndexView, DetailView, DetailTaskView


app_name = 'project'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:project_id>/', DetailView.as_view(), name='detail'),
    path('<int:project_id>/<int:task_id>/', DetailTaskView.as_view(), name='task'),
]
