# Generated by Django 4.2.5 on 2023-09-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_lang_categori_maincategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lang_categori',
            options={'ordering': ['Tittle'], 'verbose_name': 'Специальности', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterField(
            model_name='lang_categori',
            name='Tittle',
            field=models.CharField(max_length=50, verbose_name='Специальность'),
        ),
    ]
