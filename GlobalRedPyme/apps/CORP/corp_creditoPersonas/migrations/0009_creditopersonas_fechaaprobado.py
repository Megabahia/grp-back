# Generated by Django 3.1.7 on 2022-03-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp_creditoPersonas', '0008_auto_20220311_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditopersonas',
            name='fechaAprobado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
