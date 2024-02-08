from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        
    def __str__(self):
        return self.name    

