from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
 
from crypt.models import CryptRecData
from charge.models import ChargeRecData
from clutch.models import ClutchRecData
from credit.models import CreditRecData
from chronicle.models import ChronicleRecData
from create.models import CreateRecData
from civil.models import CivilRecData
 
class RegistrationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    firstname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"))
    lastname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Last Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

    class Meta:
        model = User
        fields = ("username",)
        
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        self.instance.email = self.cleaned_data.get('email')
        self.instance.first_name = self.cleaned_data.get('firstname')
        self.instance.last_name = self.cleaned_data.get('lastname')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class CryptReviewForm(forms.ModelForm):
	class Meta:
		model = CryptRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(CryptReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class ChargeReviewForm(forms.ModelForm):
	class Meta:
		model = ChargeRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(ChargeReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class ClutchReviewForm(forms.ModelForm):
	class Meta:
		model = ClutchRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(ClutchReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class CreditReviewForm(forms.ModelForm):
	class Meta:
		model = CreditRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(CreditReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class CreateReviewForm(forms.ModelForm):
	class Meta:
		model = CreateRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(CreateReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class ChronicleReviewForm(forms.ModelForm):
	class Meta:
		model = ChronicleRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(ChronicleReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class CivilReviewForm(forms.ModelForm):
	class Meta:
		model = CivilRecData
		fields = ('score','is_selected','reviewer_1','reviewer_2','reviewer_3')

	def __init__(self, *args, **kwargs):
                super(CivilReviewForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"
                self.fields['reviewer_1'].label = "Panel Member 1(not HR)"
                self.fields['reviewer_2'].label = "Panel Member 2(not HR)"
                self.fields['reviewer_3'].label = "Panel Member HR"

class CryptScoreForm(forms.ModelForm):
	class Meta:
		model = CryptRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(CryptScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ChargeScoreForm(forms.ModelForm):
	class Meta:
		model = ChargeRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(ChargeScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ClutchScoreForm(forms.ModelForm):
	class Meta:
		model = ClutchRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(ClutchScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CreditScoreForm(forms.ModelForm):
	class Meta:
		model = CreditRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(CreditScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CreateScoreForm(forms.ModelForm):
	class Meta:
		model = CreateRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(CreateScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class ChronicleScoreForm(forms.ModelForm):
	class Meta:
		model = ChronicleRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(ChronicleScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

class CivilScoreForm(forms.ModelForm):
	class Meta:
		model = CivilRecData
		fields = ('is_selected',)

	def __init__(self, *args, **kwargs):
                super(CivilScoreForm, self).__init__(*args, **kwargs)
                self.fields['is_selected'].label = "Selected for next round?"

