# Generated by Django 4.2.5 on 2023-09-30 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_main_categori_remove_lang_categori_maincategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='lang_categori',
            name='MainCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.main_categori', verbose_name='Категория софта'),
            preserve_default=False,
        ),
    ]
