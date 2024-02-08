from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User , verbose_name=("USER"), on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        
    def __str__(self):
        return self.name    

