from django import forms
from django.template.defaultfilters import mark_safe
from django.forms.formsets import BaseFormSet
from captcha.fields import ReCaptchaField

 
from clutch.models import ClutchRecData, File
from clutch.models import Question
from clutch.models import Answer
 

class ClutchForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    class Meta:
        model = ClutchRecData
        fields = ('name','rollno','mobileno','email')
        fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(ClutchForm, self).__init__(*args, **kwargs)
        self.fields['name'].label     = "Your Name"
        self.fields['email'].label    = "Your E-mail"
        self.fields['rollno'].label   = "Your Roll No"
        self.fields['mobileno'].label = "Your Mobile No"


class QuestionForm(forms.Form):
        def __init__(self, *args, **kwargs):
                self.page=kwargs.pop('page')
                super(QuestionForm, self).__init__(*args, **kwargs)               
                for p in Question.objects.filter(page=self.page):
                        # generate extra fields in the number specified via extra_fields
                        self.fields['extra_field_{index}'.format(index=p.id)] = forms.CharField(widget=forms.Textarea,required = True)
                        self.fields['extra_field_{index}'.format(index=p.id)].label = p.question
                        self.fields['extra_field_{index}'.format(index=p.id)].page = p.page
						
class ClutchFileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ('file',)
		fields_required = ('file',)


