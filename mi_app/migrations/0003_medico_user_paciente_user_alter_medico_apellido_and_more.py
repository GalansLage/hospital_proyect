# Generated by Django 5.0.3 on 2024-03-18 06:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0002_alter_cita_table_alter_medico_table_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medico',
            name='Apellido',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='Especialidad',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='Nombre',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Apellido',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Genero',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Nombre',
            field=models.TextField(null=True),
        ),
    ]
