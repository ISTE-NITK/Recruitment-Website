from django import forms
 
from crypt.models import CryptRecData
from charge.models import ChargeRecData
from clutch.models import ClutchRecData
from credit.models import CreditRecData
from chronicle.models import ChronicleRecData
from create.models import CreateRecData
from civil.models import CivilRecData
 

class CryptScoreForm(forms.ModelForm):
	class Meta:
		model = CryptRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(CryptScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ChargeScoreForm(forms.ModelForm):
	class Meta:
		model = ChargeRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(ChargeScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ClutchScoreForm(forms.ModelForm):
	class Meta:
		model = ClutchRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(ClutchScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CreditScoreForm(forms.ModelForm):
	class Meta:
		model = CreditRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(CreditScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CreateScoreForm(forms.ModelForm):
	class Meta:
		model = CreateRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(CreateScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ChronicleScoreForm(forms.ModelForm):
	class Meta:
		model = ChronicleRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(ChronicleScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CivilScoreForm(forms.ModelForm):
	class Meta:
		model = CivilRecData
		fields = ('score','is_selected',)

	def __init__(self, *args, **kwargs):
                super(CivilScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

