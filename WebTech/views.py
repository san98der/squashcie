from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main_page(request):
	return render(request, 'index.html')

def sign_in(request):
	return render(request, 'sign_in.html')

	
