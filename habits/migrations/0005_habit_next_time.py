# Generated by Django 5.0 on 2024-07-13 09:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habit_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='next_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата следующего выполнения'),
            preserve_default=False,
        ),
    ]
