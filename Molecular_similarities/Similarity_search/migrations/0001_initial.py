# Generated by Django 4.1 on 2023-11-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IUPAC', models.CharField(max_length=1000, unique=True)),
                ('description', models.CharField(max_length=10000, unique=True)),
                ('SMILES', models.CharField(max_length=1000, unique=True)),
                ('Name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
    ]