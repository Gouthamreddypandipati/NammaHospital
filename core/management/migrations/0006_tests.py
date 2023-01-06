# Generated by Django 4.1.4 on 2022-12-29 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_docterpatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test_to_be_taken', models.CharField(blank=True, max_length=300, null=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.doctor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.usermodel')),
            ],
        ),
    ]
