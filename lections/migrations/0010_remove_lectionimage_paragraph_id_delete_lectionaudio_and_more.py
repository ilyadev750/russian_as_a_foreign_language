# Generated by Django 4.2.7 on 2024-05-13 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lections', '0009_alter_lection_in_production'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectionimage',
            name='paragraph_id',
        ),
        migrations.DeleteModel(
            name='LectionAudio',
        ),
        migrations.DeleteModel(
            name='LectionImage',
        ),
    ]