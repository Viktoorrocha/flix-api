# Generated by Django 5.1.7 on 2025-04-01 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='stars',
        ),
    ]
