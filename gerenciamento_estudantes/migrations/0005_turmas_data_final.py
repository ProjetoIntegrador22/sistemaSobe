# Generated by Django 5.1.3 on 2024-11-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estudantes', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmas',
            name='data_final',
            field=models.DateField(blank=True, null=True),
        ),
    ]
