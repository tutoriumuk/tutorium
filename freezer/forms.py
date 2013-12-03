from django import forms
from tutorium.freezer.models import *
from django.core.exceptions import ValidationError

class RecruitForm(forms.ModelForm):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))

	class Meta:
		model = tutor
		fields = ('firstname', 'lastname', 'email',)


