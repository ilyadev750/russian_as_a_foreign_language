# Generated by Django 4.2.7 on 2024-05-13 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='paragraph_id',
        ),
        migrations.RemoveField(
            model_name='lectionaudio',
            name='paragraph_id',
        ),
        migrations.RemoveField(
            model_name='lectionimage',
            name='paragraph_id',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='LectionAudio',
        ),
        migrations.DeleteModel(
            name='LectionImage',
        ),
    ]
