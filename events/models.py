from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model

User = get_user_model()



class Event(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField()
    description = models.TextField()
    # event_pk = models.IntegerField(primary_key = True)
    # ADD A PICTURE FOR EVENT LATER
    organizer = models.ForeignKey(User, on_delete= models.CASCADE, related_name='events')

    def __str__(self):
        return self.name

# class Booking(models.Model):
#     # available_seats = ??
#     # booking_pk = models.IntegerField(primary_key = True)
#     event = models.ForeignKey(Event, on_delete= models.CASCADE, related_name='bookings')
#     user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='bookings')
#     date = models.DateField() 
    # how many seat

