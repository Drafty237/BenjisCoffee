# Generated by Django 4.1 on 2024-05-19 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidos', '0004_rewards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rewards',
            name='Status',
        ),
        migrations.AlterField(
            model_name='rewards',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
