from django.db.models import Count
from ..models import Club

def get_top_clubs(limit=5):
    """Get top clubs based on event count."""
    return Club.objects.annotate(
        event_count=Count('event')
    ).order_by('-event_count')[:limit]

def get_club_stats(club):
    """Get statistics for a specific club."""
    return {
        'event_count': club.event_set.count(),
        'member_count': club.members.count(),
        'active_events': club.event_set.filter(status='upcoming').count()
    }