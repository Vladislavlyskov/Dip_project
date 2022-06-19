from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    text = models.TextField()
    price = models.FloatField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now=True)