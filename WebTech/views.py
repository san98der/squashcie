from django.shortcuts import render

def main_page(request):
	return render(request, 'index.html')

def matches_page(request):
	return render(request, 'matches.html')

def ranking_page(request):
	return render(request, 'ranking.html')

def results_page(request):
	return render(request, 'results.html')

def thank_you_page(request):
	return render(request, 'thank_you.html')
