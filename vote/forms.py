from dataclasses import fields
from django import forms 
from .models import Vote
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm , UsernameField
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth.models import User


class createPollForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['question','option_one','option_two','option_three']
        labels = {'question':'Question','option_one':'Option One,','option_two':'Option Two','option_three':'Option Three'}
        widgets = {'question':forms.TextInput(attrs={'class':'form-control'}),
        'option_one':forms.TextInput(attrs={'class':'form-control'}),
        'option_two':forms.TextInput(attrs={'class':'form-control'}),
        'option_three':forms.TextInput(attrs={'class':'form-control'})
        }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password' , widget= forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password' , widget= forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        labels = {'first_name':'First name','last_name':'Last name','email':'Email'}

        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))