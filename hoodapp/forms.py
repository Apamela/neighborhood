
from .models import Neighborhood,Business,Profile,Post
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name',)

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name','location')

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','email','business_location')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)
