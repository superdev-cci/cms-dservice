from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('env_check', views.env_check)
]