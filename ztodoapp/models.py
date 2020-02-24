from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
	task = models.CharField(max_length=25)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	task_status = models.BooleanField()


	def __repr__(self):
		return '<Todo {} {} {}'.format(
			self.task, 
			self.user,
			self.task_status
			)


