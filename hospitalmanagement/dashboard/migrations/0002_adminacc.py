# Generated by Django 3.2 on 2024-05-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAcc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Ad', models.CharField(max_length=100)),
                ('Soyad', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
