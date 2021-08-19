from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login





class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ('username','email','password1','password2')



class UserLoginForm(forms.Form):
	email = forms.EmailField(label='Eamil',widget=forms.EmailInput())
	password = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'placeholder':'password'}))


	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email,password=password):
				raise forms.ValidationError('invalid login check your password email')





class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['company_name','company_profile','profile_picture','official_email']




class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = Account
		fields = ['username','email']
