from django import forms
from django.template.defaultfilters import mark_safe
from django.forms.formsets import BaseFormSet
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
 
from credit.models import CreditRecData
from credit.models import Question
from credit.models import Answer
 

class CreditForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = CreditRecData
        fields = ('name','rollno','mobileno','email')
        fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(CreditForm, self).__init__(*args, **kwargs)
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
                        # generate extra fields in the number specified via extra_fields
                        self.fields['extra_field_{index}'.format(index=p.id)] = forms.CharField(widget=forms.Textarea,required = True)
                        self.fields['extra_field_{index}'.format(index=p.id)].label = p.question
                        self.fields['extra_field_{index}'.format(index=p.id)].page = p.page
