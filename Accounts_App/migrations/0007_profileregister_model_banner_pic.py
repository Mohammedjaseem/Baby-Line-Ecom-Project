# Generated by Django 4.1 on 2022-08-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts_App', '0006_profileregister_model_mobile_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileregister_model',
            name='banner_pic',
            field=models.ImageField(blank=True, upload_to='profile/banner_pics/'),
        ),
    ]
