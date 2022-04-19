
from django.urls import path
from . import views

urlpatterns = [
    path('project', views.HomeForm, name="homeproject"),
    path('postdata', views.HomePostData, name='PostData'),
    path('viewspost', views.DataForm, name='viewspost'),
]