from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    date = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField()

    # Event organizer
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    tickets = models.IntegerField(default=1)

    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.event.title}"


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.user.username