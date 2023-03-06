from django.urls import path
from . views import *

urlpatterns = [
    path('', InputView.as_view(), name='home')
]