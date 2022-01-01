from django.contrib.auth import login
from .views import home, item_list, register_user, login_user
from django.urls import path

app_name = 'market'

urlpatterns = [
	path('', home, name='home'),
	path('item/', item_list, name='items'),
	path('register/', register_user, name='register'),
	path('login/', login_user, name='login')
]