from django.conf.urls import url
from . import views

urlpatterns=[
              url(r'^profile/(\d+)',views.profile,name='profile'),
]