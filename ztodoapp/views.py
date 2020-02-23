from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def login(request):
	return JsonResponse({'msg': 'in login page'})
	# return render(request, 'in the login page')