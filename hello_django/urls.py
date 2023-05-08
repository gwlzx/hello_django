"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from one.views import *
from user.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('one.urls', namespace="contact")),
    url(r'^register/', include('register.urls', namespace="register")),
    url(r'^login/', login, name='login'),
    url(r'^reg', reg, name='reg'),
    url(r'^tmp', tmp, name='tmp'),
    url(r'^captcha', verify_code, name='verify_code'),
    url(r'getpage/(\d+)$', get_page, name="page"),

]
