# Generated by Django 3.2.25 on 2024-08-24 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='datosusuarios',
            table='datos_usuarios',
        ),
        migrations.AlterModelTable(
            name='indentificador',
            table='indentificador',
        ),
        migrations.AlterModelTable(
            name='permisos',
            table='permisos',
        ),
        migrations.AlterModelTable(
            name='typeuser',
            table='type_user',
        ),
        migrations.CreateModel(
            name='TypePermisosUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permisos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.permisos')),
                ('type_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.typeuser')),
            ],
            options={
                'db_table': 'tipo_permisos_usuarios',
                'unique_together': {('type_user_id', 'permisos_id')},
            },
        ),
    ]
