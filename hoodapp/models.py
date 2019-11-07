from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField
# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    
    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

    def update_neighborhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.neighborhood_name}'

class Profile(models.Model):
    name = models.CharField(max_length=20,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio= models.TextField(max_length=254,blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=30,blank=True)
    neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE,null=True,blank=True)

    def assign_neighborhood(self,neighborhood):
        self.neighborhood = neighborhood
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'

class Business(models.Model):
    name = models.CharField(max_length=30)
    business_location = models.CharField(max_length=30,blank=True)
    business_neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
    def update_business(self,name):
        self.name = name
        self.save()

    def __str__(self):
        return f'{self.name}'


class EmergencyContacts(models.Model):
    name = models.CharField(max_length=30)
    contacts = models.CharField(max_length=20)
    email = models.EmailField()
    neighborhood_contact = models.ForeignKey('Neighborhood',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.email}'


class Post(models.Model):
    title = models.CharField(max_length=40)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    post_hood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    def __str__(self):
        return f'{self.title},{self.post_hood.neighborhood_name}'

