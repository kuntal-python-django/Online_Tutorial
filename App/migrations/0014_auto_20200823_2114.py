# Generated by Django 2.2 on 2020-08-23 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20200507_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='description',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='i_o',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='timing',
        ),
    ]
