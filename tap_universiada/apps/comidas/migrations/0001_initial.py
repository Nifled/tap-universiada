# Generated by Django 2.0.2 on 2018-03-15 18:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.IntegerField(choices=[(1, 'Desayuno'), (2, 'Comida'), (3, 'Cena')])),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True)),
                ('nombres', models.CharField(max_length=85)),
                ('apellido_p', models.CharField(max_length=45, verbose_name='Apellido Paterno')),
                ('apellido_m', models.CharField(max_length=45, verbose_name='Apellido Materno')),
                ('estatus', models.BooleanField(default=True, editable=False)),
                ('institucion', models.CharField(max_length=85)),
                ('tipo', models.IntegerField(choices=[(1, 'Deportista'), (2, 'Entrenador'), (3, 'Juez'), (4, 'Delegado'), (5, 'Coordinador'), (6, 'Comisionado Técnico'), (7, 'Médico'), (8, 'Comité Organizador')])),
                ('ultima_comida', models.BooleanField(default=False, editable=False)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comidas.Disciplina')),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comidas.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='comida',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comidas.Participante'),
        ),
    ]
