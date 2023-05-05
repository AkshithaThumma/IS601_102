from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ...
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('event_list', views.event_list, name='event_list'),
    path('<int:event_id>/signup/', views.event_signup, name='event_signup'),
    path('<int:event_id>/unsignup/', views.event_unsignup, name='event_unsignup'),
    path('create_event/', views.create_event, name='create_event')
]
