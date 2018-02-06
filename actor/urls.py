from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^actors/$', views.ActorList.as_view()),
]