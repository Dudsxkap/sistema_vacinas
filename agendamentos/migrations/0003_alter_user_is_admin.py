# Generated by Django 3.2.3 on 2021-05-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0002_auto_20210530_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
    ]
