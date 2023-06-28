from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('delete/<int:id>/',dete_user,name='delete'),
    path('update/<int:id>/',update_user,name='update'),
]