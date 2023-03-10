from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class user_room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
