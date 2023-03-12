from django.urls import path
from . import views
urlpatterns=[
    path('',views.view_booking,name = 'booking/'),
    path('book',views.book,name = "book/"),
    path('bookedlrdownload/<str:name>',views.bookedlrdownload,name="bookedlr/"),
]