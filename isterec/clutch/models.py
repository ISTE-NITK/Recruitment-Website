from django.db import models
import os


	
class ClutchRecData(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False,default='')
    rollno = models.CharField(max_length=15, blank=False, null=False,default='')
    mobileno = models.CharField(max_length=20, blank=False, null=False,default='')
    email = models.CharField(max_length=50, blank=False, null=False,default='')
    
    def __str__ (self):
        return self.rollno

class Question(models.Model):
    page = models.IntegerField()
    question = models.TextField()
    creation = models.DateField(auto_now_add = True)
    
    def __str__ (self):
        return self.question

class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question)
    creator = models.ForeignKey(ClutchRecData)
    is_correct = models.BooleanField(default = False)

    def __str__ (self):
        return self.answer

class File(models.Model):
    file = models.FileField(upload_to='files/clutch/%Y/%m/%d')
    creator = models.ForeignKey(ClutchRecData)

    def __unicode__(self):
        return self.file.name

    def filename(self):
        return os.path.basename(self.file.name)
