# Generated by Django 4.2.8 on 2024-02-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_remove_fidelidade_agenda_remove_fidelidade_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fidelidade',
            name='descricao',
            field=models.CharField(max_length=250, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='fidelidade',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome da Fidelidade'),
        ),
    ]