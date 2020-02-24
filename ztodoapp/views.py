from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
from .forms import RegisterForm, AddTaskForm


# Create your views here.

# def home(request):
# 	return JsonResponse({'msg': 'in home page'})
# 	# return render(request, 'in the login page')

def home(request):
	if request.method == 'POST':

		form = AddTaskForm(request.POST)

		if form.is_valid():
			task = Todo(
				task=request.POST['task'],
				user_id=request.user.id,
				task_status=False # pending todo
				)			
			task.save()

			# print('12345')

			return HttpResponseRedirect(reverse('todo:home'))
		else:
			messages.error(request, form.errors)

	tasks = Todo.objects.filter(user_id=request.user.id)
	print(tasks)

	form = AddTaskForm()
	return render(request, 'todo/home.html', {'tasks': tasks})

def loginUser(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			tasks = Todo.objects.filter(user_id=request.user.id)
			return render(request, 
				'todo/home.html', 
				{
					'user': request.user.username,
					'tasks': tasks,
				})
		else:
			messages.error(request, 'Authentication Failed')

	return render(request, 'todo/login.html')

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect(reverse('todo:login'))

def register(request):
	if request.method == 'POST':

		form = RegisterForm(request.POST)

		if form.is_valid():
			user = User.objects.create_user(
				first_name=request.POST['first_name'],
				last_name=request.POST['last_name'],
				email=request.POST['email'],
				username=request.POST['email'],
				password=request.POST['password'],
				date_joined=timezone.now(),
				is_superuser=False,
				is_staff=False,
				is_active=True
				)			
			user.save()

			return HttpResponseRedirect(reverse('todo:login'))
		else:
			messages.error(request, form.errors)

	form = RegisterForm()
	return render(request, 'todo/register.html')





