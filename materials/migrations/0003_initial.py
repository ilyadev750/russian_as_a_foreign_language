# Generated by Django 4.2.7 on 2024-05-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lections', '0013_adminlectionaction_number'),
        ('materials', '0002_remove_image_paragraph_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='media/lection_audio', verbose_name='Аудиозапись')),
                ('audio_name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Аудиозапись',
                'verbose_name_plural': 'Аудиозаписи',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/lection_images', verbose_name='Изображение')),
                ('image_name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='LectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.image', verbose_name='Изображение')),
                ('paragraph_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lections.paragraph', verbose_name='Параграф')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='LectionAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.audio', verbose_name='Аудиозапись')),
                ('paragraph_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lections.paragraph', verbose_name='Параграф')),
            ],
            options={
                'verbose_name': 'Аудиозапись',
                'verbose_name_plural': 'Аудиозаписи',
            },
        ),
    ]
