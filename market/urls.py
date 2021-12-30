from django.urls import path
from .views import home

app_name = 'market'

urlpatterns = [
	path('', home, name='home'),
]