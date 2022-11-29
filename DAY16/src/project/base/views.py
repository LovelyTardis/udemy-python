from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Task


class LoginUser(LoginView):
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterUser(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterUser, self).get(*args, **kwargs)


class PendingList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(done=False).count()
        context["count"] = context["tasks"].filter(done=False).count()

        search_text = self.request.GET.get("search-text") or ""
        if search_text:
            context["tasks"] = context["tasks"].filter(title__icontains=search_text)

        context["search_text"] = search_text
        return context


class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "title",
        "description",
        "done"
    ]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "done"
    ]
    success_url = reverse_lazy("tasks")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
