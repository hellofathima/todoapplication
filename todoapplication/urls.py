"""
URL configuration for todoapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

from task.views import TodoCreateView
from task.views import TodoListView
from task.views import TodoDetailView
from task.views import TodoDeleteView,TodoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ',TodoCreateView.as_view(),name="todo-add"),
    path('todo/all/',TodoListView.as_view(),name="todo-list"),
    path('todo/<int:pk>',TodoDetailView.as_view(),name="todo-details"),
    path('todo/<int:pk>/remove/',TodoDeleteView.as_view(),name="todo-delete"),
    path('todo/<int:pk>/change/',TodoUpdateView.as_view(),name="todo-change"),
    path("",include("remainder.urls")),

    path("api/",include("taskapi.urls")),
    path("api/v1.1/",include("reminderapi.urls")),
    

]

