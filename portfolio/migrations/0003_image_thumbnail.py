# Generated by Django 3.1.1 on 2020-09-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200913_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
