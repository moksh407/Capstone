# Generated by Django 2.0 on 2018-11-21 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20181121_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='year_of_graduation',
            new_name='graduation_year',
        ),
    ]
