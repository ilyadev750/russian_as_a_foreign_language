# Generated by Django 4.2.7 on 2024-05-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0003_admindictionaryaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindictionaryaction',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер действия'),
        ),
    ]