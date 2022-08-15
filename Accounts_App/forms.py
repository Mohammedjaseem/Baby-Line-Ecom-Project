from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models as user_models
from django.utils.translation import gettext_lazy as _

class NewUserForm(UserCreationForm):
    email     = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Please enter your email'}))
    username  = forms.CharField(required=True, label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Please enter your user name'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'}))
    password2 = forms.CharField(required=True, label="confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user       = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        username   = self.cleaned_data['username']
        
        if commit:
            user.save()
        return user

class DateInput(forms.DateInput):
    input_type = 'date'

class profile_register(forms.ModelForm):
    class Meta:
        model  = user_models.profileregister_model
        fields = '__all__'
        dob    = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2020)))
        labels = {
            'user_id'      : _('User Id'),
            'name'         : _('Full Name'),
            'mobile_number': _('Mobile Number'),
            'dob'          : _('Date of Birth'),
            'gender'       : _('Choose Gender'),
            'pincode'      : _('Pin Code'),
            'address'      : _('Address'),
            'dp'           : _('Upload your profile picture')
        }
        widgets = {
            'user_id'      : forms.HiddenInput(),
            'name'         : forms.TextInput(attrs={'placeholder': 'Please enter your name'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Please enter your mobile number'}),
            'dob'          : DateInput(),
            'gender'       : forms.Select(attrs={'class': 'form-control'}),
            'pincode'      : forms.NumberInput(attrs={'placeholder': 'Please enter your pin code'}),
            'address'      : forms.TextInput(attrs={'placeholder': 'Please enter your address'}),
            'dp'           : forms.FileInput,
        }

 