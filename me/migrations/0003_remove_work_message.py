# Generated by Django 5.1.1 on 2025-01-12 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_category_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='message',
        ),
    ]
