# Generated by Django 2.0.12 on 2019-04-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0014_remove_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='entry_fee',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='graduation_year',
            field=models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028)], default=2019, verbose_name='year'),
        ),
    ]
