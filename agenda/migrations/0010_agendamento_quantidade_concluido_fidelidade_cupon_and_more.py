

from datetime import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_alter_agendamento_criado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='quantidade_concluido',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fidelidade',
            name='cupon',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='criado_em',
            field=models.DateTimeField(default=datetime(2024, 1, 28)),
        ),
    ]
