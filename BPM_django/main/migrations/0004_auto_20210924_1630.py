# Generated by Django 3.2.7 on 2021-09-24 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210924_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userBirth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='userHeight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='userWeight',
            field=models.IntegerField(default=0),
        ),
    ]
