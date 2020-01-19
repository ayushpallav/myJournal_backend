from django import forms

from django.contrib.auth.models import User

from journals.models import Profile


class UserForm(forms.ModelForm):
	password = forms.CharField()
	class Meta:
		model = User
		fields = (
			'username',
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
