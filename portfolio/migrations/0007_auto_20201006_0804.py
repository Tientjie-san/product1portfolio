# Generated by Django 3.1.1 on 2020-10-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20201006_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='interest',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
