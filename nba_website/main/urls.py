from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/<int:player_id>/', views.player_analysis, name='player_analysis'),
]
