# Generated by Django 4.0.2 on 2022-05-19 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
