# Generated by Django 5.1 on 2024-08-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebServerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturereading',
            name='humidity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
