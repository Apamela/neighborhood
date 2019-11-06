# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#***********************************class for the user profile************************************************************************************************

class Profile(models.Model):
      name = models.CharField(max_length=30,blank=True)
      user= models.Foreignkey(User,on_delete=models.CASCADE)
      location = models.CharField(max_length=30,blank=True)
      neighborhood = models.Foreignkey(Neighborhood ,on_delete=models.CASCADE,null=True,blank=True)

        def save_profile(self):
            self.save()
        def delete_Profile(self):
            self.delete()
        def __str__(self):
            return f'{self.user.username}'
     