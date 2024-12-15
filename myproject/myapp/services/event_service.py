from datetime import datetime
from ..models import Event, EventRegistration

def get_upcoming_events(limit=5):
    """Get upcoming events."""
    return Event.objects.filter(
        date__gte=datetime.now(),
        status='upcoming'
    ).order_by('date')[:limit]

def check_event_capacity(event):
    """Check if event has available spots."""
    current_registrations = EventRegistration.objects.filter(event=event).count()
    return current_registrations < event.max_participants

def register_user_for_event(event, user):
    """Register a user for an event."""
    if check_event_capacity(event):
        registration, created = EventRegistration.objects.get_or_create(
            event=event,
            user=user
        )
        return created
    return False