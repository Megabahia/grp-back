# Generated by Django 3.1.7 on 2022-02-17 15:46

import apps.MDM.mdm_prospectosClientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProspectosClientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, max_length=150, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('tipoCliente', models.CharField(blank=True, max_length=150, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=150, null=True)),
                ('facebook', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter', models.CharField(blank=True, max_length=150, null=True)),
                ('instagram', models.CharField(blank=True, max_length=150, null=True)),
                ('correo1', models.EmailField(blank=True, max_length=150, null=True)),
                ('correo2', models.EmailField(blank=True, max_length=150, null=True)),
                ('pais', models.CharField(blank=True, max_length=255, null=True)),
                ('provincia', models.CharField(blank=True, max_length=255, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('canal', models.CharField(blank=True, max_length=150, null=True)),
                ('codigoProducto', models.CharField(blank=True, max_length=150, null=True)),
                ('nombreProducto', models.CharField(blank=True, max_length=150, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('tipoPrecio', models.CharField(blank=True, max_length=250, null=True)),
                ('nombreVendedor', models.CharField(blank=True, max_length=250, null=True)),
                ('confirmacionProspecto', models.CharField(blank=True, max_length=250, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=apps.MDM.mdm_prospectosClientes.models.upload_path)),
                ('identificacion', models.CharField(blank=True, max_length=13, null=True)),
                ('nombreCompleto', models.CharField(blank=True, max_length=255, null=True)),
                ('empresa_id', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('state', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
