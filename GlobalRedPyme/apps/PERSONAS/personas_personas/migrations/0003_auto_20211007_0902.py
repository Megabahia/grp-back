# Generated by Django 3.1.7 on 2021-10-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas_personas', '0002_auto_20211007_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='user_id',
            field=models.CharField(max_length=250),
        ),
    ]
