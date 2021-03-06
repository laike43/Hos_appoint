# Generated by Django 2.1.5 on 2019-03-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=12)),
                ('department', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('infirmary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('seat_num', models.CharField(max_length=20)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('brief', models.TextField(max_length=300)),
                ('seatsnum', models.IntegerField(default=0)),
            ],
        ),
    ]
