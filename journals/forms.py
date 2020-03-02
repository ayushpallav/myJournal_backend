from django import forms

from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from journals.models import Profile


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'password',
			'email'
		)


class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = (
			'primary_cell',
			'profile_pic'
		)


class MakeEntryForm(forms.Form):
	entry = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 5}))
