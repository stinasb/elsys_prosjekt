# Generated by Django 3.1.1 on 2022-02-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punkt_text', models.CharField(max_length=200)),
                ('punkt_oppdatert', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_text', models.CharField(max_length=200)),
                ('measure', models.IntegerField(default=0)),
                ('punkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punkt.punkt')),
            ],
        ),
    ]
