from django.contrib import admin
from django.urls import path
from List.views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post/<int:pk>', detail, name='detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('author/<str:username>', author, name='author'),
    path('register/', register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='List/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='List/logout.html'), name='logout'),
    path('post/delete/', post_delete_all, name='post_delete_all'),
    path('post/<int:pk>/done/', post_done, name='post_done'),
    path('post/<int:pk>/undone/', post_not_done, name='post_not_done'),


]
