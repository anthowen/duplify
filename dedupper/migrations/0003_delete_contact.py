# Generated by Django 2.0.7 on 2018-08-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dedupper', '0002_repcontact_misc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
    ]