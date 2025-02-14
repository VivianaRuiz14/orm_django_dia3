# Generated by Django 5.0.6 on 2024-06-25 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(default='', unique=True)),
                ('eliminada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='subtarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(default='')),
                ('eliminada', models.BooleanField(default=False)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtareas', to='dia3.tarea')),
            ],
        ),
    ]
