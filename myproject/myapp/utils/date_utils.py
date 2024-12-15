from datetime import datetime

def format_countdown(target_date):
    """Format countdown time."""
    now = datetime.now()
    if target_date < now:
        return "Event Started"
    
    delta = target_date - now
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return f"{days}d {hours}h {minutes}m"