# Generated by Django 3.2.25 on 2024-08-27 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20240824_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indentificador',
            name='TypeUserId',
            field=models.ForeignKey(db_column='type_user_id', on_delete=django.db.models.deletion.CASCADE, to='backend.typeuser'),
        ),
    ]
