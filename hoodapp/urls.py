from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.welcome, name='welcome'),

    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^add_business/',views.add_business,name='add_business'),
    url(r'^change_neighborhood/(\d+)',views.change_neighborhood,name='change_neighborhood'),
    url(r'^search/',views.search,name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)