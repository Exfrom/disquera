# Generated by Django 3.0.14 on 2023-07-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20230728_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='apellidosArtista',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artista',
            name='emailArtista',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artista',
            name='estadoArtista',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='artista',
            name='fotoArtista',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artista',
            name='noDocumento',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='artista',
            name='nombreArtista',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artista',
            name='tipoDocumento',
            field=models.CharField(max_length=25),
        ),
    ]
