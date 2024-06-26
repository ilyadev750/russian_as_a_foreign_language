# Generated by Django 4.2.7 on 2024-04-02 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lections', '0002_alter_content_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RemoveField(
            model_name='lection',
            name='category_id',
        ),
        migrations.AddField(
            model_name='lection',
            name='profile_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lections.specialization', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='specialization_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Профиль'),
        ),
    ]
