# Generated by Django 4.0.5 on 2022-06-11 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='detination',
            new_name='destination',
        ),
    ]