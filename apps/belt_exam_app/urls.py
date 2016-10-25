from django.conf.urls import url
from . import views
from login_and_registration_app.views import index, register, login


urlpattern =[
    url(r'^$', views.index)
]
