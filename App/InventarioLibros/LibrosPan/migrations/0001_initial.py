# Generated by Django 4.2 on 2024-11-14 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibrosPan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('costoactual', models.BigIntegerField(blank=True, null=True, verbose_name='CostoActual')),
                ('existencia', models.BigIntegerField(blank=True, null=True, verbose_name='Existencia')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Categorias.categoria', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'LibrosPan',
            },
        ),
    ]
