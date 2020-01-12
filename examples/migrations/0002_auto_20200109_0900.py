# Generated by Django 3.0.1 on 2020-01-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=50)),
                ('publication_date', models.DateField(null=True)),
                ('IP_address', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('device_type', models.PositiveSmallIntegerField(choices=[(1, 'Router'), (2, 'SmartPhone'), (3, 'Desktop'), (4, 'Laptop'), (5, 'Tablet'), (6, 'Modem')])),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
