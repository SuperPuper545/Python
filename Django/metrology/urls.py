from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add-cont/', CreateMetr.as_view(), name='add_cont'),
]