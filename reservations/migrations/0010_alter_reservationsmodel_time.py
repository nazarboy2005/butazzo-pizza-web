# Generated by Django 5.0.6 on 2024-05-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_alter_reservationsmodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationsmodel',
            name='time',
            field=models.CharField(max_length=16),
        ),
    ]
