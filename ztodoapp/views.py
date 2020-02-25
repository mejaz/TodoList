from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
from .forms import RegisterForm, AddTaskForm, LoginForm


@login_required
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
			return HttpResponseRedirect(reverse('todo:home'))
		else:
			messages.error(request, form.errors)

	tasks = Todo.objects.filter(user_id=request.user.id)

	form = AddTaskForm()
	return render(request, 'todo/home.html', {'tasks': tasks})

def loginUser(request):
	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():

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
		else:
			messages.error(request, form.errors)

	return render(request, 'todo/login.html')

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect(reverse('todo:login'))

def register(request):
	if request.method == 'POST':

		form = RegisterForm(request.POST)

		print('email')
		print(request.POST.get('email'))
		print('object')
		print(User.objects.filter(username=request.POST.get('email')))

		if form.is_valid():
			if User.objects.filter(username=request.POST.get('email')).count() == 0:
				print('#'* 30)
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
				messages.error(request, "username already exists.")
		else:
			messages.error(request, form.errors)

	form = RegisterForm()
	return render(request, 'todo/register.html')

def deleteTask(request, id):

	Todo.objects.filter(pk=id).delete()
	return HttpResponseRedirect(reverse('todo:home'))

def completeTask(request, id):
	t = Todo.objects.get(pk=id)

	if t.task_status == True:
		t.task_status = False
		t.save()
	else:
		t.task_status = True
		t.save()

	return HttpResponseRedirect(reverse('todo:home'))

def editTask(request, id):
	if request.method == 'POST':

		form = AddTaskForm(request.POST)

		if form.is_valid():
			t = Todo.objects.get(pk=id)
			t.task = request.POST['task']
			t.save()
			return HttpResponseRedirect(reverse('todo:home'))
		else:
			messages.error(request, form.errors)

	form = AddTaskForm()
	return render(request, 'todo/editForm.html')	





