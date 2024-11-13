# Generated by Django 5.1.3 on 2024-11-13 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento_estudantes', '0002_estudantes_ano_final_estudantes_ano_inicio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='estudantes',
            name='curso_id',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='curso_id',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='curso_id',
        ),
        migrations.RemoveField(
            model_name='relatorioausenciaestudante',
            name='estudante_id',
        ),
        migrations.RemoveField(
            model_name='feedbackestudante',
            name='estudante_id',
        ),
        migrations.RemoveField(
            model_name='relatoriofrequencia',
            name='estudante_id',
        ),
        migrations.RemoveField(
            model_name='notificacoesestudante',
            name='estudante_id',
        ),
        migrations.RemoveField(
            model_name='feedbackfuncionario',
            name='funcionario_id',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='materia_id',
        ),
        migrations.RemoveField(
            model_name='relatoriofrequencia',
            name='frequencia_id',
        ),
        migrations.RemoveField(
            model_name='notificacoesfuncionario',
            name='funcionario_id',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='funcionario_id',
        ),
        migrations.RemoveField(
            model_name='relatorioausenciafuncionario',
            name='funcionario_id',
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
        migrations.DeleteModel(
            name='RelatorioAusenciaEstudante',
        ),
        migrations.DeleteModel(
            name='FeedbackEstudante',
        ),
        migrations.DeleteModel(
            name='Estudantes',
        ),
        migrations.DeleteModel(
            name='NotificacoesEstudante',
        ),
        migrations.DeleteModel(
            name='FeedbackFuncionario',
        ),
        migrations.DeleteModel(
            name='Frequencia',
        ),
        migrations.DeleteModel(
            name='RelatorioFrequencia',
        ),
        migrations.DeleteModel(
            name='NotificacoesFuncionario',
        ),
        migrations.DeleteModel(
            name='Materias',
        ),
        migrations.DeleteModel(
            name='Funcionarios',
        ),
        migrations.DeleteModel(
            name='RelatorioAusenciaFuncionario',
        ),
    ]
