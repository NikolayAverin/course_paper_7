# Generated by Django 5.0 on 2024-07-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите ваш телеграм ИД",
                max_length=255,
                null=True,
                verbose_name="ИД телеграм",
            ),
        ),
    ]