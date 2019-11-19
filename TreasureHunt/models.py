from django.db import models
# from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import uuid




class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    # coordinates = models.PointField()
    players = ArrayField(ArrayField(models.CharField(max_length=50)))
    items = ArrayField(models.CharField(max_length=50))
    exits = ArrayField(models.CharField(max_length=5))
    cooldown = models.IntegerField(default=0)
    errors = ArrayField(models.CharField(max_length=50))
    messages = ArrayField(models.CharField(max_length=50))
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default=0)
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)



