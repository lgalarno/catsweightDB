# Generated by Django 2.0.1 on 2018-02-05 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0002_auto_20180203_0127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measure',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='measure',
            name='number',
        ),
    ]
