# Generated by Django 5.0 on 2023-12-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_anuncio_expira_alter_anuncio_tempo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='pesquisas',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.CharField(blank=True, default='unid.', max_length=10),
        ),
    ]