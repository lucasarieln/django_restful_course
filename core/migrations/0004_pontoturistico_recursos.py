# Generated by Django 4.1.6 on 2023-02-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0002_alter_recursos_options'),
        ('core', '0003_alter_pontoturistico_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='recursos',
            field=models.ManyToManyField(to='recursos.recursos'),
        ),
    ]
