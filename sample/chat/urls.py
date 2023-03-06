from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('groups/',views.rooms, name='rooms'),
    path('groups/add/',views.addrooms, name='addrooms'),
    path('groups/del/',views.delrooms, name='delrooms'),
    path('groups/<slug:slug>/', views.room, name='room'),
    path('groups/<slug:slug>/<int:id>/', views.roomusers, name='roomusers'),
    path('groups/<slug:slug>/<int:id>/add/', views.addusers, name='addusers'),
    path('groups/<slug:slug>/<int:id>/del/', views.delusers, name='delusers'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
]