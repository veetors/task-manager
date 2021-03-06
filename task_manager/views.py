from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from task_manager.filters import TaskFilter, UserTaskFilter
from task_manager.forms import (
    SignupForm,
    TaskCreationForm,
    TaskForm,
    UserUpdateForm,
)
from task_manager.models import Tag, Task


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('task_list'))
        return redirect(reverse_lazy('login'))


# User
class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = _('Account was created for %(username)s')


class UserUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/user_update_form.html'
    success_url = reverse_lazy('home')
    success_message = _('Profile was successfully updated')


class UserPasswordUpdate(
    SuccessMessageMixin,
    LoginRequiredMixin,
    auth_views.PasswordChangeView,
):
    template_name = 'registration/user_password_update_form.html'
    success_message = _('Password was successfully updated')

    def get_success_url(self):
        return reverse_lazy('user_edit', args=(self.request.user.id,))


# Tags
class TagList(LoginRequiredMixin, ListView):
    model = Tag


class TagCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('tag_list')
    success_message = _('Tag "%(name)s" was successfully created')


class TagUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tag_list')
    success_message = _('Name "%(name)s" was successfully updated')


class TagDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    success_message = _('Tag deleted successfully')

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


# Tasks
class TaskList(LoginRequiredMixin, ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_filter = TaskFilter(self.request.GET)
        context['task_filter'] = task_filter
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('task_list')
    success_message = _('Task "%(name)s" was successfully created')

    def get_initial(self):
        user = self.request.user
        return {
            'creator': user,
            'assigned_to': user,
        }


class TaskUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = '_update_form'
    success_message = _('Task "%(name)s" was successfully updated')

    def get_success_url(self):
        return reverse_lazy('task_detail', args=(self.object.id,))


class TaskDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = _('Task deleted successfully')

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


class UserTaskList(TaskList):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_filter = UserTaskFilter(self.request.user, self.request.GET)
        context['task_filter'] = task_filter
        return context
