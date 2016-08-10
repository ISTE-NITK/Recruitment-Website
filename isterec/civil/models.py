from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

	
class CivilRecData(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False,default='')
    roll_regex = RegexValidator(regex=r'^(\d{2}|\d{8})([a-z]{2}|[A-Z]{2})\d{2,3}([a-z]{1}|[A-Z]{1})?$', message="Please enter a valid Roll number.")
    rollno = models.CharField(max_length=15, validators=[roll_regex], blank=False, null=False,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobileno = models.CharField(max_length=16, validators=[phone_regex], blank=False, null=False,default='+91')
    email = models.EmailField(blank=False, null=False,default='')
    score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False, null=False,default=0)
    is_selected = models.BooleanField(default = False)
    date_created = models.DateTimeField(default=timezone.now)
    
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
    creator = models.ForeignKey(CivilRecData)
    is_correct = models.BooleanField(default = False)

    def __str__ (self):
        return self.answer

