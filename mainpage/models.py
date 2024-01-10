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