"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from task_manager import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.UserCreate.as_view(), name='signup'),

    path('accounts/', include('django.contrib.auth.urls')),

    path(
        'users/<int:pk>/edit/',
        views.UserUpdate.as_view(),
        name='user_edit',
    ),
    path(
        'users/<int:pk>/password/edit',
        views.UserPasswordUpdate.as_view(),
        name='user_password_edit',
    ),

    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tags/new/', views.TagCreate.as_view(), name='tag_new'),
    path('tags/<int:pk>/edit/', views.TagUpdate.as_view(), name='tag_edit'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),

    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('tasks/new/', views.TaskCreate.as_view(), name='task_new'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path(
        'tasks/<int:pk>/edit/',
        views.TaskUpdate.as_view(),
        name='task_edit',
    ),
    path(
        'tasks/<int:pk>/delete/',
        views.TaskDelete.as_view(),
        name='task_delete',
    ),
    path('tasks/my/', views.UserTaskList.as_view(), name='user_task_list'),

    path('admin/', admin.site.urls),
]
