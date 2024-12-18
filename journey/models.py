from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


STATUS = (
    ('Nice', 'Nice'),
    ('Naughty', 'Naughty'), 
    )


# Create your models here.

class Household(models.Model):
    """
    Stores a single Household related to :model:`auth.user` 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Kid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    family = models.ForeignKey(Household, null=False, blank=False, on_delete=models.CASCADE, related_name='kids')
    behavior = models.CharField(choices=STATUS, default='Nice', max_length=20)

    def __str__(self):
        return self.name
