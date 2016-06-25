from django import forms
 
from crypt.models import UploadFile
 

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadFile
		fields = ('name','rollno','mobileno','email','body')
		fields_required = ('name','rollno','mobileno','email','body')

	def __init__(self, *args, **kwargs):
                super(UploadFileForm, self).__init__(*args, **kwargs)
                self.fields['name'].label     = "Your name     :"
                self.fields['email'].label    = "Your E-mail   :"
                self.fields['rollno'].label   = "Your Roll No  :"
                self.fields['mobileno'].label = "Your Mobile No:"
                self.fields['body'].label     = "What do you want to join crypt?"
