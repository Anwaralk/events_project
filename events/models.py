from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    # user_field = models.IntegerField(primary_key = True)


    def __str__(self):
        return self.username

User = get_user_model()



class Event(models.Model):
    event_name = models.CharField(max_length = 50)
    event_date = models.DateField()
    event_description = models.TextField()
    event_pk = models.IntegerField(primary_key = True)
    # ADD A PICTURE FOR EVENT LATER
    # user_field = models.ForeignKey(User, on_delete= models.CASCADE, related_name='events')

    def __str__(self):
        return self.event_name, self.event_date

class Booking(models.Model):
    # available_seats = ??
    booking_pk = models.IntegerField(primary_key = True)
    event_field = models.ForeignKey(Event, on_delete= models.CASCADE, related_name='bookings')
    user_field = models.ForeignKey(User, on_delete= models.CASCADE, related_name='events')
    booking_date = models.DateField()

