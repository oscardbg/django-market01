from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from market.models import Item

def home(request):
	return render(request, 'market/index.html')

def item_list(request):
	item_list = Item.objects.all()
	context = {
		'item_list': item_list
	}
	return render(request, 'market/item_list.html', context)

def register_user(request):
	return render(request, 'market/register.html')

def login_user(request):
	return render(request, 'market/login.html')