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

	# def save(self):
	# 	try:
	# 		user = User.objects.create_user(
	# 			first_name=self.fname,
	# 			last_name=self.last_name,
	# 			email=self.email,
	# 			username=self.email,
	# 			password=self.password,
	# 			date_joined=datetime.datetime.now(),
	# 			is_superuser=False,
	# 			is_staff=False,
	# 			is_active=True
	# 			)
	# 		user.save()
	# 		return {'result': 0, 'obj': user }
	# 	except Exception as e:
	# 		print(e)
	# 		return {'result': 1, 'msg': str(e) }






