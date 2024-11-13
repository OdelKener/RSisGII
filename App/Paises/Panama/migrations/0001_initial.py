# Generated by Django 4.2 on 2024-11-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SucursalPan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Panama', editable=False, max_length=255)),
                ('codigo', models.IntegerField(default=4, editable=False)),
            ],
            options={
                'verbose_name': 'SucursalPan',
            },
        ),
    ]
