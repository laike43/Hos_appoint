# Generated by Django 2.1.5 on 2019-03-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30, unique=True)),
                ('department_message', models.TextField()),
                ('beizhu1', models.CharField(max_length=50)),
                ('beizhu2', models.CharField(max_length=50)),
                ('beizhu3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=30, unique=True)),
                ('hospital_location', models.CharField(max_length=50)),
                ('hospital_rank', models.IntegerField()),
                ('hospital_message', models.TextField()),
                ('beizhu1', models.CharField(max_length=200)),
                ('beizhu2', models.CharField(max_length=200)),
                ('beizhu3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=30)),
                ('department_name', models.CharField(max_length=30)),
                ('agree', models.BooleanField(default=True)),
            ],
        ),
    ]
