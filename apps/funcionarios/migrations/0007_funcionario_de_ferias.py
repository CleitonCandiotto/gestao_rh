# Generated by Django 3.2.12 on 2022-04-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_alter_funcionario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
    ]
