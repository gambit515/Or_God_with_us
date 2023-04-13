# Generated by Django 4.1.7 on 2023-04-13 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_alter_anketa_author_alter_anketa_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa',
            name='Author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор анкеты'),
        ),
    ]
