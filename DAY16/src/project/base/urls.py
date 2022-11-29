from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import \
    PendingList,\
    DetailTask,\
    CreateTask,\
    EditTask,\
    DeleteTask,\
    LoginUser,\
    RegisterUser

urlpatterns = [
    path("", PendingList.as_view(), name="tasks"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("task/<int:pk>", DetailTask.as_view(), name="task"),
    path("create-task/", CreateTask.as_view(), name="create-task"),
    path("edit-task/<int:pk>", EditTask.as_view(), name="edit-task"),
    path("delete-task/<int:pk>", DeleteTask.as_view(), name="delete-task"),
]
