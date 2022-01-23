from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('traveler/<int:traveler_id>/', views.traveler, name='traveler'),
    path('choice/<int:traveler_id>/<int:choice_id>/', views.choice, name='choice'),
    path('new/<int:user_id>/<int:parent_id>/', views.new, name='new'),
]
