# Generated by Django 4.1.4 on 2022-12-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('total_experience', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('specialization', models.CharField(blank=True, max_length=128, null=True)),
                ('Hospital_name', models.CharField(blank=True, max_length=128, null=True)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
