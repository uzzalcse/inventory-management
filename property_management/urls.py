from django.urls import path

from . import views

urlpatterns = [
    path("emon/", views.index, name="index"),
    path("zaber/", views.hello_from_zaber, name="zaber_vai"),
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("vote/<int:question_id>/", views.vote, name="vote"),
]