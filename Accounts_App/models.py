from pyexpat import model
from django.db import models
from django import forms
from django.urls import  reverse
from django.contrib.auth.models import User
##mobile number validation



class profileregister_model(models.Model):
    user_id       = models.CharField(max_length=100)
    name          = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    dp            = models.ImageField(upload_to='profile_pics/', blank=True)
    dob           = models.DateField(null=True, blank=True)
    gender_choose = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    gender = models.CharField(
        max_length = 20,
        choices    = gender_choose,
        default    = 'Choose your Gender')
    pincode        = models.CharField(max_length=10)
    address        = models.CharField(max_length=500)
    

    def __str__(self):
        return (self.name)