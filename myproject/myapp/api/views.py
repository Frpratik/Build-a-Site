from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..models import Event
from ..services import event_service

def event_capacity(request, event_id):
    """API endpoint for event capacity."""
    event = get_object_or_404(Event, id=event_id)
    current_registrations = event.eventregistration_set.count()
    
    return JsonResponse({
        'current': current_registrations,
        'max': event.max_participants,
        'available': event_service.check_event_capacity(event)
    })