from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

class Profile(models.Model):
    user = models.ForeignKey(User , verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name:"),max_length=80)
    subtitle = models.CharField(_("zu meiner person"),max_length=50)
    address = models.CharField(_("stadt"),max_length=50)
    number_phone = models.CharField(_("telefon"),max_length=50)
    working_hours = models.CharField(_("btriebszeiten"),max_length=50)
    waiting_time = models.IntegerField(_("wartezeit"),blank=True,null=True)
    doctor = models.CharField(_("doktor"),max_length=50)
    who_i = models.TextField(_("wer ich bin:"),max_length=50)
    price = models.IntegerField(_("untersuchengs price:"),blank=True,null=True)
    image = models.ImageField(_("personal foto"),upload_to='profile',blank=True,null=True)
    Specialist_doctor = models.CharField(_("spezialisiert"),max_length=100)
    slug = models.SlugField(_("slug"),blank=True)
                                  
    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
        
    def __str__(self):
        return '%s' %(self.name)
    
    def save(self, *args ,**kwargs):
        if not self.slug:
            self.slug = slugify (self.user.username)
        super(Profile,self).save( *args ,**kwargs)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile , sender=User)       