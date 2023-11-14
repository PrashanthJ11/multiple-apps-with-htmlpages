from django.urls import path
from gt.views import *
app_name='anything'
urlpatterns=[
    path('gill/',gill,name='gill'),
]
