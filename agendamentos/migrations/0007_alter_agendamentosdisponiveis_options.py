# Generated by Django 3.2.3 on 2021-06-02 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0006_alter_agendamentos_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamentosdisponiveis',
            options={'ordering': ['local_vacinacao', 'data', 'horario', '-num_vagas'], 'verbose_name': 'Agendamentos Disponíveis', 'verbose_name_plural': 'Agendamentos Disponíveis'},
        ),
    ]
