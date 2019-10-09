# Generated by Django 2.2.6 on 2019-10-09 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rnc', models.IntegerField(verbose_name='RNC')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Carreer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('enrollment', models.IntegerField(default=0, verbose_name='Inscritos')),
                ('graduates', models.IntegerField(default=0, verbose_name='Graduados')),
                ('openingDate', models.DateField(blank=True, null=True, verbose_name='Fecha de Apertura')),
                ('closingDate', models.DateField(blank=True, null=True, verbose_name='Fecha de Cierre')),
                ('credits', models.IntegerField(default=0, verbose_name='Creditos')),
                ('degree', models.CharField(choices=[('undergraduate', 'Grado'), ('graduate', 'Postgrado')], max_length=13, null=True, verbose_name='Nivel')),
                ('univesity', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='UniversityCarrersFK', to='csvintegration.University')),
            ],
        ),
    ]