from django import forms
 
from crypt.models import CryptRecData
from crypt.models import File
 

class CryptForm(forms.ModelForm):
	class Meta:
		model = CryptRecData
		fields = ('name','rollno','mobileno','email','body')
		fields_required = ('name','rollno','mobileno','email','body')

	def __init__(self, *args, **kwargs):
                super(CryptForm, self).__init__(*args, **kwargs)
                self.fields['name'].label     = "Your name"
                self.fields['email'].label    = "Your E-mail"
                self.fields['rollno'].label   = "Your Roll No"
                self.fields['mobileno'].label = "Your Mobile No"
                self.fields['body'].label     = "What do you want to join crypt?"

class CryptFileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ('file',)
		fields_required = ('file',)
