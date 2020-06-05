from django.urls import path
from django.conf.urls import url
from .views import partners, index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('partners/', partners, name='partners'),
]
