# Generated by Django 4.2 on 2024-11-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('costoactual', models.BigIntegerField(blank=True, null=True, verbose_name='CostoActual')),
                ('existencia', models.BigIntegerField(blank=True, null=True, verbose_name='Existencia')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Categorias.categoria', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Libros',
            },
        ),
    ]
