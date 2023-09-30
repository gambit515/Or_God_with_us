# Generated by Django 4.2.5 on 2023-09-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_lang_categori_maincategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=50, verbose_name='Категории софта')),
            ],
            options={
                'verbose_name': 'Основная категория',
                'verbose_name_plural': 'Основная категория',
                'ordering': ['Tittle'],
            },
        ),
        migrations.RemoveField(
            model_name='lang_categori',
            name='MainCategory',
        ),
    ]
