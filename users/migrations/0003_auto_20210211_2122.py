# Generated by Django 3.1.6 on 2021-02-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_session_duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
