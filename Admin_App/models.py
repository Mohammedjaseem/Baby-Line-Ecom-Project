from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class category_model(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    image       = models.ImageField(upload_to='images/category', blank=True)

    def __str__(self):
        return self.name

class subcategory_model(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    category    = models.ForeignKey(category_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class age_category_model(models.Model):
    age         = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.age

class product_model(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    image       = models.ImageField(upload_to='images/product', blank=True)
    price       = models.IntegerField()
    offer_price = models.IntegerField(blank=True, null=True)
    category    = models.ForeignKey(category_model, on_delete=models.CASCADE)
    gender_slt  = (
        ('Male','Male'),
        ('Female','Female'),
        ('Unisex','Unisex')
    )
    gender = models.CharField(
        max_length = 20,
        choices    = gender_slt,
        default    = 'Choose your Gender')
    subcategory    = models.ForeignKey(subcategory_model(), on_delete=models.CASCADE)
    key_features   = models.TextField(blank=True, null=True)
    Note           = models.TextField(blank=True, null=True)
    Brand          = models.CharField(max_length=100, blank=True, null=True)
    size           = models.ForeignKey(age_category_model, on_delete=models.CASCADE)
    stock          = models.IntegerField(default=0)
    available      = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name