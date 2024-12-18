# Generated by Django 4.2 on 2024-11-14 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LibrosPan', '0001_initial'),
        ('Panama', '0001_initial'),
        ('LibrosHon', '0001_initial'),
        ('Nicaragua', '0001_initial'),
        ('TipoEntrada', '0001_initial'),
        ('LibrosCos', '0001_initial'),
        ('Libros', '0001_initial'),
        ('Hondura', '0001_initial'),
        ('CostaRica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'EntradasDetalles',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaentrada', models.CharField(max_length=100, verbose_name='FechaEntrada')),
                ('sucursalid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Nicaragua.sucursal', verbose_name='Sucursal')),
                ('sucursalidcos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='CostaRica.sucursalcos', verbose_name='SucursalCos')),
                ('sucursalidhon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Hondura.sucursalhon', verbose_name='SucursalHon')),
                ('sucursalidpan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panama.sucursalpan', verbose_name='SucursalPan')),
                ('tipoentrada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='TipoEntrada.tipoentrada', verbose_name='TipoEntrada')),
            ],
            options={
                'verbose_name': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='DetalleEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costoactual', models.BigIntegerField(blank=True, null=True, verbose_name='CostoActual')),
                ('cantidad', models.BigIntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Entrada.entrada', verbose_name='Entrada')),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Libros.libro', verbose_name='Libro')),
                ('librocos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='LibrosCos.libroscos', verbose_name='LibroCos')),
                ('librohon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='LibrosHon.libroshon', verbose_name='LibroHon')),
                ('libropan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='LibrosPan.librospan', verbose_name='LibroPan')),
            ],
            options={
                'verbose_name': 'DetallesEntradas',
            },
        ),
    ]
