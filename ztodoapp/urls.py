from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
	path('', views.login, name='login'),
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('home/', views.home, name='home'),
	path('register/', views.register, name='register'),
]