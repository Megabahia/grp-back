# Generated by Django 3.1.7 on 2022-04-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_productos', '0002_auto_20211001_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='codigoDescuento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
