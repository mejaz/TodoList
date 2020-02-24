from django import forms


class RegisterForm(forms.Form):

	# class Meta:
	# 	model = User
	# 	fields = [
	# 		'first_name',
	# 		'last_name',
	# 		'email',
	# 		'password'
	# 	]
	first_name = forms.CharField(label='first_name', max_length=50)
	last_name = forms.CharField(label='last_name', max_length=50)
	email = forms.CharField(label='email', max_length=100)
	password = forms.CharField(label='password', max_length=50)

class AddTaskForm(forms.Form):
	task = forms.CharField(label='task', max_length=500)





