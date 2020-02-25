from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('home/', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('deleteTask/<int:id>/', views.deleteTask, name='deleteTask'),
	path('completeTask/<int:id>/', views.completeTask, name='completeTask'),
	path('editTask/<int:id>/', views.editTask, name='editTask'),
]