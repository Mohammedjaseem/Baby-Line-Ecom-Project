# Generated by Django 4.1 on 2022-08-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0005_remove_subcategory_model_image_product_model_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='Brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='Note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_model',
            name='key_features',
            field=models.TextField(blank=True, null=True),
        ),
    ]
