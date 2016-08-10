from django import forms
from django.template.defaultfilters import mark_safe
from django.forms.formsets import BaseFormSet
from captcha.fields import ReCaptchaField

 
from create.models import CreateRecData
from create.models import Question
from create.models import Answer
 

class CreateForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    class Meta:
        model = CreateRecData
        fields = ('name','rollno','mobileno','email')
        fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label     = "Your Name"
        self.fields['email'].label    = "Your E-mail"
        self.fields['rollno'].label   = "Your Roll No"
        self.fields['mobileno'].label = "Your Mobile No"
        self.fields['captcha'].label = "Are you human?"


class QuestionForm(forms.Form):
        def __init__(self, *args, **kwargs):
                self.page=kwargs.pop('page')
                super(QuestionForm, self).__init__(*args, **kwargs)               
                for p in Question.objects.filter(page=self.page):
                        if p.id ==2:
                                self.fields['url_field'] = forms.URLField(initial="http://",required = True)
                                self.fields['url_field'].label = p.question
                                self.fields['url_field'].page = p.page

                        else:
                                self.fields['extra_field_{index}'.format(index=p.id)] = forms.CharField(widget=forms.Textarea,required = True)
                                self.fields['extra_field_{index}'.format(index=p.id)].label = p.question
                                self.fields['extra_field_{index}'.format(index=p.id)].page = p.page
