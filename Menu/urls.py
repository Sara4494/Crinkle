from django.urls import path
from .views import MenuListView 

urlpatterns = [
    path('menu-cards/', MenuListView.as_view(), name='menu-cards'),
    
]

