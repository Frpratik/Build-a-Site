from django.urls import path
from . import views
from .api import views as api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', views.register_event, name='register_event'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    
    # API endpoints
    path('api/event-capacity/<int:event_id>/', api_views.event_capacity, name='api_event_capacity'),
]