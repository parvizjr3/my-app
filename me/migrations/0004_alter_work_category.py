# Generated by Django 5.1.1 on 2025-01-12 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_remove_work_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='me.category'),
        ),
    ]
