# Generated by Django 4.0.3 on 2022-03-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_alter_documento_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='documeto',
            field=models.FileField(default=' ', upload_to='documentos', verbose_name='Documento'),
            preserve_default=False,
        ),
    ]