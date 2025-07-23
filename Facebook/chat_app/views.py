from urllib import request
from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
	names = ['Garima', 'Sanjay', 'Sanjana', 'Sanjay']
	return render(request, 'chat_app/home.html', {'names': names})

def about(request):
	info = {
		'name': 'Garima',
		'address': 'Jorpati'
	}
	return render(request, 'chat_app/about.html', {'my_info': info})
