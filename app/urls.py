 
from django.urls import path  
from .views import *

urlpatterns = [
   path('', home , name ='home'),
     path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    
]
 