from django.conf.urls import  url
from user2 import views

urlpatterns = [
    url(r'^',views.index()),
]
