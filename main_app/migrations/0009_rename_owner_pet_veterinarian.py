# Generated by Django 5.0.1 on 2024-01-23 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_pet_rxs_checkin_rxs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='owner',
            new_name='veterinarian',
        ),
    ]
