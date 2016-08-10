from django import forms

from crypt.models import CryptRecData
from crypt.models import File, Question, Answer
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CryptForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = CryptRecData
        fields = ('name','rollno','mobileno','email')
        fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(CryptForm, self).__init__(*args, **kwargs)
        self.fields['name'].label     = "Your name"
        self.fields['email'].label    = "Your E-mail"
        self.fields['rollno'].label   = "Your Roll No"
        self.fields['mobileno'].label = "Your Mobile No"
        self.fields['captcha'].label = "Please prove you're not a robot"

class CryptFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)
        fields_required = ('file',)

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page=kwargs.pop('page')
        super(QuestionForm, self).__init__(*args, **kwargs)
        for p in Question.objects.filter(page=self.page):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=p.id)] = forms.CharField(widget=forms.Textarea,required = True)
            self.fields['extra_field_{index}'.format(index=p.id)].label = p.question
            self.fields['extra_field_{index}'.format(index=p.id)].page = p.page
