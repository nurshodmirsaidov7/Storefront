from .views import say_hello
from django.urls import path

urlpatterns = [
    path("hello/", say_hello)
]
