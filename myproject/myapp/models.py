from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    logo = models.ImageField(upload_to='club_logos/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='club_members')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    max_participants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='upcoming')

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)
    feedback = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(null=True, blank=True, choices=[
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ])

    class Meta:
        unique_together = ['event', 'user']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    points = models.PositiveIntegerField(default=0)
    interests = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username