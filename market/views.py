from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from market.models import Item

def home(request):
	return render(request, 'market/index.html')

def item_list(request):
	item_list = Item.objects.filter(owner=None)
	item_owned = Item.objects.filter(owner=request.user)

	if request.method == 'POST':
		
		# Item buying code
		bitem = request.POST.get('buyed_item')
		if bitem:
			buyed_item = bitem
			itemb_obj = Item.objects.get(name=buyed_item)
			if itemb_obj:
				itemb_obj.owner = request.user
				itemb_obj.save()
				messages.success(request, f'Congrats, you have bought the item {itemb_obj.name} ')
		
		# Item selling code
		sitem = request.POST.get('selled_item')
		if sitem:
			selled_item = sitem
			items_obj = Item.objects.get(name=selled_item)
			if items_obj:
				items_obj.owner = None
				items_obj.save()
				messages.success(request, f'Congrats, you have sold the item {items_obj.name} ')
		
		return redirect('market:items')

	context = {
		'item_list': item_list,
		'item_owned': item_owned
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
			return redirect('market:items')
		else:
			messages.error(request, form.errors)
			return redirect('market:register')

	return render(request, 'market/register.html')

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f'You are logged in as {user.username} ')
			return redirect('market:items')
		else:
			messages.error(request, 'Username or password is incorrect, try again')
			return redirect('market:login')

	return render(request, 'market/login.html')

def logout_user(request):
	logout(request)
	messages.success(request, 'You have been logout...')
	return redirect('market:login')