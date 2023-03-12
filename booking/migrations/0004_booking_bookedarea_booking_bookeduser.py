# Generated by Django 4.1.1 on 2023-03-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_charges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookedarea',
            field=models.CharField(default='admin', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='bookeduser',
            field=models.CharField(default='admin', max_length=10),
            preserve_default=False,
        ),
    ]