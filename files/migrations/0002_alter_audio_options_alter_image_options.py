# Generated by Django 4.2.7 on 2024-04-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'verbose_name': 'Аудиозапись', 'verbose_name_plural': 'Аудиозаписи'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
    ]