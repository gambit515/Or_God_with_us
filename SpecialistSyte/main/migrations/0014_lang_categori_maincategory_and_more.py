# Generated by Django 4.2.5 on 2023-09-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_anketa_soft_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='lang_categori',
            name='MainCategory',
            field=models.CharField(default='Пусто', max_length=50, verbose_name='Главная категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lang_categori',
            name='Tittle',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
    ]
