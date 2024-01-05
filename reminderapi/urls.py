from django.urls import path
from reminderapi import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("todos",views.TodoViewsetView,basename="v1Todos")
urlpatterns=[

path("register/",views.UserCreationView.as_view(),name="register"),

]+router.urls