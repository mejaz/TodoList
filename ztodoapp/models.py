from django.db import models

# Create your models here.


class Todo(models.Model):
	task = models.CharField(max_length=500)
	task_added_time = models.DateTimeField()
	task_status = models.BooleanField()


	def __repr__(self):
		return '<Todo {} {} {} {}'.format(
			self.task, 
			self.task_added_time,
			self.task_status
			)


