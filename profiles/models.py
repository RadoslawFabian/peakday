from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)  # waga w kg
    height = models.PositiveIntegerField(null=True, blank=True)  # wzrost w cm

    def __str__(self):
        return f"{self.user.username} Profile"
