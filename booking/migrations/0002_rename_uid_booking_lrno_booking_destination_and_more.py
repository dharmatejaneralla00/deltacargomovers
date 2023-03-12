# Generated by Django 4.1.1 on 2023-03-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='uid',
            new_name='lrno',
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
