from django.urls import path

from users.views import members, viewfuntion

urlpatterns =[
    #path('members/', views.members, name='members'),
    path('',members,name="home"),
    path('about/',viewfuntion,name="about"),
]