from django.db import models


# Create your models here.

class Model(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    comment = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}, {self.price}, {self.amount}, {self.comment}"


class Comment(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
    text = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.age}, {self.text}"