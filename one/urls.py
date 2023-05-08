from django.conf.urls import url
from one.views import *


urlpatterns = [
    url(r'^index$', index, name="index"),
    url(r'^$', home, name='home'),
    url(r'^get_data$', get_data, name='get_data'),
    url(r'^add_people$', add_people, name='add_people'),
    url(r'^save_data$', add_people, name='save_data'),
    url(r'^peoples$', people_list, name='peoples'),
    url(r'^people/(?P<pk>\d+)', people_detail, name='people_detail'),
    url(r'^delete/(\d+)$', delete_people, name='delete'),
    url(r'^save_pic$', save_pic, name='save_pic'),
]
