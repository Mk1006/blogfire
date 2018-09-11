from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
""" this models used to store branstore's customer data """

class BloggerProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    email_id = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    home_town = models.CharField(max_length=150, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    hobbies = models.CharField(max_length=200,null=True, blank=True)
    
    
class BloggerPic(models.Model):
    bloguser=models.ForeignKey(BloggerProfile,on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=2000,null=True, blank=True)
    


@receiver(post_save, sender=User)
def update_blogger_profile(sender, instance, created, **kwargs):
    if created:
        BloggerProfile.objects.create(user=instance)
    instance.bloggerprofile.save()