from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login



class DateInput(forms.DateInput):
	input_type = 'date'




class JobPostingForm(forms.ModelForm):
	
	class Meta:
		widgets = {'expiration_date':DateInput()}
		model = Job_Posting
		exclude = ['status','employer']



class ApplicantForm(forms.ModelForm):
	firstName = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	lastName  = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	email     = forms.CharField(label='',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
	upload    = forms.FileField(label='upload CV',widget=forms.FileInput(attrs={'placeholder':'CV'}))


	class Meta:
		model = Applicant
		fields = ['firstName','lastName','email','upload']

