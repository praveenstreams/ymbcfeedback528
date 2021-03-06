# Generated by Django 3.0.5 on 2021-05-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentfeedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_oncourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
                ('sem', models.IntegerField(max_length=10)),
                ('content', models.CharField(max_length=20)),
                ('coverage', models.CharField(max_length=20)),
                ('application', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('clarity', models.CharField(max_length=20)),
                ('metirial', models.CharField(max_length=20)),
                ('effort', models.CharField(max_length=20)),
                ('overall', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='feedback_onfaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
                ('sem', models.IntegerField(max_length=10)),
                ('teacher', models.CharField(max_length=20)),
                ('knowledge', models.CharField(max_length=20)),
                ('communication', models.CharField(max_length=20)),
                ('Commitment', models.CharField(max_length=20)),
                ('interest', models.CharField(max_length=20)),
                ('integratingskill', models.CharField(max_length=20)),
                ('integratecontent', models.CharField(max_length=20)),
                ('accessibility', models.CharField(max_length=20)),
                ('cordination', models.CharField(max_length=20)),
                ('provision', models.CharField(max_length=20)),
                ('overall', models.CharField(max_length=20)),
            ],
        ),
    ]
