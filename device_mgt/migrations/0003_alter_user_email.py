# Generated by Django 4.2.7 on 2023-11-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_mgt', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
