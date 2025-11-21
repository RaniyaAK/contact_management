from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)      
    phone = models.CharField(max_length=20, null=True, blank=True)    
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'No Name'}"
