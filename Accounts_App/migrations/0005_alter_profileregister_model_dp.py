# Generated by Django 4.1 on 2022-08-13 09:34

import django.conf.urls.static
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts_App', '0004_alter_profileregister_model_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileregister_model',
            name='dp',
            field=models.ImageField(blank=True, upload_to=django.conf.urls.static.static),
        ),
    ]
