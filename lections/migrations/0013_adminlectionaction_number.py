# Generated by Django 4.2.7 on 2024-05-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lections', '0012_adminlectionaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlectionaction',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер действия'),
        ),
    ]
