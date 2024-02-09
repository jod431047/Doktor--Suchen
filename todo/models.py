from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.ForeignKey(User , verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name:"),max_length=50)
    who_i = models.TextField(_("who I am:"),max_length=250)
    price = models.IntegerField(_("disclosure price:"))
    image = models.ImageField(_("personal poto"),upload_to='profile')
                                  
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        
    def __str__(self):
        return '%s' %(self.name)
    
    
