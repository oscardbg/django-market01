from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
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
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, f'You have registered successfully, welcome {user.username} ')
			return redirect('market:home')
		else:
			messages.error(request, form.errors)
			return redirect('market:register')

	return render(request, 'market/register.html')

def login_user(request):
	return render(request, 'market/login.html')