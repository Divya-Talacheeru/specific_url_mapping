from django.urls import path
from hyd.views import *

app_name='nothing'

urlpatterns=[
    path('devpadikkal/',devpadikkal,name='devpadikkal'),
]