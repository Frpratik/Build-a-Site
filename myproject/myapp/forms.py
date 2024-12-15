from django import forms
from .models import Event, UserProfile
from .utils.validators import validate_future_date, validate_max_participants

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image', 'max_participants']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        validate_future_date(date)
        return date

    def clean_max_participants(self):
        max_participants = self.cleaned_data.get('max_participants')
        validate_max_participants(max_participants)
        return max_participants

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'interests']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'interests': forms.TextInput(attrs={'placeholder': 'Enter your interests (comma-separated)'}),
        }