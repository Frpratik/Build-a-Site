from ..models import UserProfile

def get_top_users(limit=50):
    """Get top users based on points."""
    return UserProfile.objects.order_by('-points')[:limit]

def update_user_points(user, points):
    """Update user points."""
    profile = UserProfile.objects.get(user=user)
    profile.points += points
    profile.save()
    return profile