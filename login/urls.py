from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login/'),
    path('dashbaoard', views.dashbaord, name='dashboard/'),
    path('logout', views.logout, name='logout/')
]
