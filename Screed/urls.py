from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('traveler/<int:traveler_id>/', views.traveler, name='traveler'),
    path('choice/<int:traveler_id>/<int:choice_id>/', views.choice, name='choice'),
    path('new/<int:user_id>/<int:parent_id>/', views.new, name='new'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
]
