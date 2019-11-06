# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def profile(request,user_id):
    user = User.objects.get(id = user_id)
    profile = UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.name = request.POST['first_name']
            profile.location = request.POST['location']
            profile.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        form = UpdateProfileForm(instance=profile)

    businesses = Business.objects.filter(owner = user).all()
    emergencies = EmergencyContacts.objects.filter(neighborhood_contact = profile.neighborhood).all()
    neighborhoods = Neighborhood.objects.all()

    return render(request,'profile.html',{'neighborhoods':neighborhoods,'businesses':businesses,'profile':profile,'form':form,'emergencies':emergencies})
