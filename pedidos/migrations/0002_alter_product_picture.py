# Generated by Django 4.1 on 2024-03-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.CharField(max_length=4000),
        ),
    ]
