from django.conf.urls import url
from register.views import *


urlpatterns = [
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^val_user$', val_user, name="val_user"),
]
