# Generated by Django 4.1.4 on 2022-12-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
