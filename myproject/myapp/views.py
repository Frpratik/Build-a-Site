from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm, UserProfileForm
from .services import event_service, club_service, user_service

def home(request):
    upcoming_events = event_service.get_upcoming_events()
    top_clubs = club_service.get_top_clubs()
    leaderboard = user_service.get_top_users(10)
    
    return render(request, 'home.html', {
        'upcoming_events': upcoming_events,
        'top_clubs': top_clubs,
        'leaderboard': leaderboard
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.club = request.user.club_set.first()
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_detail', event.id)
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_registered = event.eventregistration_set.filter(user=request.user).exists()
    
    context = {
        'event': event,
        'is_registered': is_registered,
        'club_stats': club_service.get_club_stats(event.club)
    }
    return render(request, 'event_detail.html', context)

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if event_service.register_user_for_event(event, request.user):
            messages.success(request, 'Successfully registered for the event!')
            user_service.update_user_points(request.user, 10)  # Award points for registration
        else:
            messages.error(request, 'Sorry, the event is full!')
    return redirect('event_detail', event_id)

@login_required
def leaderboard(request):
    top_users = user_service.get_top_users()
    return render(request, 'leaderboard.html', {'top_users': top_users})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    user_events = request.user.eventregistration_set.all()
    return render(request, 'profile.html', {
        'form': form,
        'user_events': user_events
    })