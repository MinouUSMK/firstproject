from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.createview,name='create'),

    path('<int:id>/',views.single_post,name='single_post'),
    path('search',views.searchview,name='search'),
]