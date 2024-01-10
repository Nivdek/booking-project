from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Published"))

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    food_type = models.CharField(max_length=20)
    about = models.TextField()
    city = models.CharField(max_length=25)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_posts"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["city"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="bookings"
    )
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    date = models.DateTimeField()
    no_of_guests = models.IntegerField(default=1)
    additional_notes = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-restaurant", "-booked_on"]

    def __str__(self):
        return f"Booking for {self.no_of_guests} at {self.restaurant}"