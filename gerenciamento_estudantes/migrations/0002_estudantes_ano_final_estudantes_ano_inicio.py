# Generated by Django 5.1.3 on 2024-11-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estudantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudantes',
            name='ano_final',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='estudantes',
            name='ano_inicio',
            field=models.DateField(null=True),
        ),
    ]
