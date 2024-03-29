# Generated by Django 4.2.7 on 2024-02-26 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization_name', models.CharField(max_length=100, unique=True, verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'специальность',
                'verbose_name_plural': 'специальности',
            },
        ),
        migrations.CreateModel(
            name='Lection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lection_name', models.CharField(max_length=50, unique=True, verbose_name='Название лекции')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lections.specialization', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'лекция',
                'verbose_name_plural': 'лекции',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_content', models.CharField(max_length=400, verbose_name='Абзац')),
                ('italic_words', models.CharField(max_length=100, verbose_name='Курсивные слова')),
                ('uppercase_words', models.CharField(max_length=100, verbose_name='Слова с заглавными буквами')),
                ('lection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lections.lection', verbose_name='Лекция')),
            ],
        ),
    ]
