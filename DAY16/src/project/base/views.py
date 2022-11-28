from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task


class PendingList(ListView):
    model = Task
    context_object_name = "tasks"


class DetailTask(DetailView):
    model = Task
    context_object_name = "task"


class CreateTask(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
