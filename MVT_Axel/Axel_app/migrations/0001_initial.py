# Generated by Django 4.0.2 on 2022-06-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('deporte_favorito', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=30)),
                ('comision', models.CharField(max_length=30)),
            ],
        ),
    ]
