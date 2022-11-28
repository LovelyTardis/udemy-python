from django.urls import path
from .views import PendingList, DetailTask, CreateTask

urlpatterns = [
    path("", PendingList.as_view(), name="pending-list"),
    path("task/<int:pk>", DetailTask.as_view(), name="task"),
    path("create-task/", CreateTask.as_view(), name="create-task"),
]
