from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



class DatedModel(models.Model):

     class Meta:
         abstract = True
 
     date_added = models.DateTimeField(auto_now_add=True,null=True)
     date_modified = models.DateTimeField(auto_now=True,null=True) 
 
class CreatedModel(models.Model):

     """
     Models that inherit this model should explicitly write functionality to
     update the created and modified since you do not have access to the
     request context inside models
     """
 
     class Meta:
         abstract = True
 
     created_by = models.ForeignKey(
         User,null=True, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_created")
     modified_by = models.ForeignKey(
         User, on_delete=models.SET_NULL, blank=True, null=True,
         related_name="%(app_label)s_%(class)s_modified")
# Create your models here.
class UserDetails(User,DatedModel,CreatedModel):
    
      name = models.CharField(max_length=266,null=True)
      phone_number = models.CharField(max_length=20, blank=True, null=True)

class language(DatedModel,CreatedModel):
 
      is_active = models.BooleanField(null=True)
      name = models.CharField(max_length=255,null=True)
      code = models.CharField(max_length=255,null=True) 
      native_name= models.CharField(max_length=255,null=True) 
      video_name=  models.CharField(max_length=255,null=True) 
      audio_name= models.CharField(max_length=255,null=True) 
      text_name= models.CharField(max_length=255,null=True)
      meeting_name =  models.CharField(max_length=255,null=True)
      reviews_name =  models.CharField(max_length=255,null=True)
      home_name = models.CharField(max_length=255,null=True)

class content(DatedModel,CreatedModel):

      language = models.ForeignKey(language,on_delete=models.CASCADE,default=None,null=True)
      video = models.FileField(upload_to="video/",max_length=255,null=True)
      audio = models.FileField(upload_to="audio/" ,max_length=250,null=True)     
      text_content = models.TextField(null=True)
      more_info = models.TextField(null=True)
      title = models.CharField(max_length=255,null=True)
      speciality = models.JSONField(blank=True, null=True)
      video_link = models.CharField(max_length=255,null=True)
      short_video = models.FileField(upload_to="short_video/",max_length=255,null=True)
      short_video_link = models.CharField(max_length=255,null=True)
      html_content = models.TextField(null=True)
      meeting_link = models.CharField(max_length=255,null=True)
      video_thumbnail_mobile  = models.ImageField(upload_to='content/video/mobile',null =True)
      video_thumbnail_desktop = models.ImageField(upload_to='content/video/desktop',null =True)
      short_video_thumbnail_mobile = models.ImageField(upload_to='content/short_video/mobile',null =True)
      short_video_thumbnail_desktop = models.ImageField(upload_to='content/short_video/desktop',null =True)