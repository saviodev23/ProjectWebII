# Generated by Django 4.2.8 on 2024-02-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_imagemservico_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fidelidade',
            name='agenda',
        ),
        migrations.RemoveField(
            model_name='fidelidade',
            name='status',
        ),
        migrations.AddField(
            model_name='fidelidade',
            name='desconto',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fidelidade',
            name='descricao',
            field=models.CharField(default='', max_length=250, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='fidelidade',
            name='nome',
            field=models.CharField(default='', max_length=50, verbose_name='Nome da Fidelidade'),
        ),
        migrations.AddField(
            model_name='fidelidade',
            name='requisito',
            field=models.IntegerField(default=0),
        ),
    ]