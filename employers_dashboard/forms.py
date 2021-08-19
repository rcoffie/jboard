from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *
from job_posting .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login






