# Generated by Django 5.1 on 2024-08-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.PositiveIntegerField(default=1, verbose_name='조회수'),
        ),
    ]
