from .views import *
from django.urls import path

urlpatterns = [
    path('register/', SignUp.as_view(), name="SignUp")    
]