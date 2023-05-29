# Generated by Django 4.1.4 on 2023-05-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hifdh_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surah', models.CharField(max_length=50)),
                ('ayah_start', models.IntegerField(max_length=50)),
                ('ayah_end', models.IntegerField(max_length=50)),
                ('mistakes', models.IntegerField(max_length=50)),
                ('stuck', models.IntegerField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('teacher', models.CharField(max_length=50)),
            ],
        ),
    ]