from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r"datos", views.VistaTareas, "tareas")

urlpatterns = [path("", include(router.urls))]
