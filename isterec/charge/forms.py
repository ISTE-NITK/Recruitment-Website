from django import forms
from django.template.defaultfilters import mark_safe
from django.forms.formsets import BaseFormSet
from captcha.fields import ReCaptchaField

 
from charge.models import ChargeRecData
from charge.models import Question
from charge.models import Answer
 

class ChargeForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
    class Meta:
    	model = ChargeRecData
    	fields = ('name','rollno','mobileno','email')
    	fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(ChargeForm, self).__init__(*args, **kwargs)
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


class QuestionForm_2(forms.Form):
        def __init__(self, *args, **kwargs):
                self.page=kwargs.pop('page')
                super(QuestionForm_2, self).__init__(*args, **kwargs)               
                for p in Question.objects.filter(page=self.page):
                        # generate extra fields in the number specified via extra_fields
                        self.fields['extra_field_{index}'.format(index=p.id)] = forms.CharField(widget=forms.Textarea,required = False)
                        self.fields['extra_field_{index}'.format(index=p.id)].label = p.question
                        self.fields['extra_field_{index}'.format(index=p.id)].page = p.page

        def clean(self):
                form_data = self.cleaned_data
                answered = 0
                for key, data in form_data.items():
                        if data != '':
                                answered += 1
                if answered == 0:
                        raise forms.ValidationError("No questions have been answered ")
                elif answered < 2:
                        raise forms.ValidationError("Only 1 question has been answered ")

                return form_data

