# Generated by Django 4.2.8 on 2024-01-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_merge_0002_usuario_imagem_0004_rename_user_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='desconto',
            field=models.IntegerField(default=0),
        ),
    ]
