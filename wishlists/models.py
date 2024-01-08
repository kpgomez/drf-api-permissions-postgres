from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Wishlist(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    toys = models.ManyToManyField("toys.Toy", blank=True)

    def __str__(self):
        return f"{self.owner}'s Wishlist"
