# Generated by Django 4.2.17 on 2025-01-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplybooksapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.CharField(max_length=60),
        ),
    ]