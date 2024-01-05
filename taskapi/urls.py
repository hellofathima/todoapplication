from django.urls import path
from taskapi import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
router = DefaultRouter()

router.register("v1/todos",views.TodoViewsetView,basename="v1Todos")
router.register("v2/todos",views.TodoViewsetView,basename="v2Todos")
# for url in router.urls:

#     print(f"url=={url}")


urlpatterns=[



#viewset router


]+router.urls