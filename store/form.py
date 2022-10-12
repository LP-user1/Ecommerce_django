from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class CustomerCreationForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'id':'username','class':'form-control  shadow-none','placeholder':'Username'}))
  email = forms.CharField(widget=forms.EmailInput(attrs={'id':'email','class':'form-control  shadow-none','placeholder':'Example:abc@gmail.com'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass1','class':'form-control  shadow-none','placeholder':'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass2','class':'form-control  shadow-none','placeholder':'Re-enter password'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
