# Generated by Django 4.1.1 on 2023-03-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_bookedarea_booking_bookeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='desc',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
    ]
