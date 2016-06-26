from django.db import models


class UploadFile(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False,default='')
	rollno = models.CharField(max_length=15, blank=False, null=False,default='')
	mobileno = models.CharField(max_length=20, blank=False, null=False,default='')
	email = models.CharField(max_length=50, blank=False, null=False,default='')
	body = models.TextField(blank=False, null=False,default='')
	file = models.FileField(upload_to='files/%Y/%m/%d')
	
	def __str__(self):
		return self.rollno