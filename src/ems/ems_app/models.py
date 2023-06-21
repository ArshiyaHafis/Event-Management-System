from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_link = models.URLField(max_length=200)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    event_image = models.ImageField(upload_to='images/')
    event_descp = models.TextField()
    event_location = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.event_name
