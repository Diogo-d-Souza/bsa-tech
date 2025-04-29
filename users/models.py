from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username
