from django.core.exceptions import ValidationError
from datetime import datetime

def validate_future_date(date):
    """Validate that a date is in the future."""
    if date < datetime.now():
        raise ValidationError('Date must be in the future')

def validate_max_participants(value):
    """Validate maximum participants."""
    if value < 1:
        raise ValidationError('Maximum participants must be at least 1')
    if value > 1000:
        raise ValidationError('Maximum participants cannot exceed 1000')