from django.urls import path
from . import views
urlpatterns=[
    path('getclientlist/<str:name>',views.ClientlistView.as_view(),name= 'getclientlist/'),
]