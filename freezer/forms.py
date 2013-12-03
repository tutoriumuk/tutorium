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

## JEFF











## ANDY

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


