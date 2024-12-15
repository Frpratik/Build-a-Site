from django.contrib import admin
from .models import Club, Event, EventRegistration, UserProfile

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'created_at')
    search_fields = ('name', 'admin__username')
    list_filter = ('created_at',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'date', 'status', 'max_participants')
    list_filter = ('status', 'date', 'club')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'registration_date', 'attended')
    list_filter = ('attended', 'registration_date')
    search_fields = ('event__title', 'user__username')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'points')
    search_fields = ('user__username', 'bio')
    list_filter = ('points',)