# Generated by Django 4.2.5 on 2023-09-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_anketa_options_alter_anketa_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otklik',
            name='BirthDate',
            field=models.CharField(max_length=500, verbose_name='Дата рождения'),
        ),
    ]
