# Generated by Django 4.2.7 on 2023-11-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('locaUsuario', models.CharField(max_length=255)),
            ],
        ),
    ]
