# Generated by Django 4.2.7 on 2023-11-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='address',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='phone',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
