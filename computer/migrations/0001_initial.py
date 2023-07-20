# Generated by Django 3.0.7 on 2023-07-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerBrands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('ram', models.PositiveSmallIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='computer.ComputerBrands')),
                ('generation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer.ComputerGeneration')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_code', models.CharField(max_length=100, unique=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computer', to='computer.ComputerGeneration')),
            ],
        ),
    ]