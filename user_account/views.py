from django.shortcuts import render,redirect
from .forms import * 
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView




# Create your views here.


def UserRegistration(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user_account:user_login')
	else:
		form = UserRegistrationForm()
	context = {'form':form}
	return render(request,'user_account/registration.html',context)


def UserLogin(request):
	form = UserLoginForm()
	if request.POST:
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email,password=password)
			if user:
				login(request, user)
				return redirect('job_posting:jobs')

	context = {'form':form}

	return render(request,'user_account/login.html',context)




def UserProfile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'your account has been updated')
			return redirect('employers_dashboard:home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
	'u_form':u_form,
	'p_form':p_form
	}




	return render(request,'user_account/profile.html',context)





class MyPasswordChangeView(PasswordChangeView):
	template_name = 'user_account/password-change.html'
	success_url   = reverse_lazy('password_change_done')




class MyPasswordResetDoneView(PasswordResetDoneView):
	template_name = 'user_account/password-reset-done.html'


def UserLogout(request):
	logout(request)
	return redirect('job_posting:jobs')





