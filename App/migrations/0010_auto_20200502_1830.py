# Generated by Django 2.2 on 2020-05-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200502_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='location',
            field=models.TextField(default=''),
        ),
    ]
