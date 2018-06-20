# Generated by Django 2.0.5 on 2018-06-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NullBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charNull', models.CharField(max_length=10, null=True)),
                ('charBlank', models.CharField(blank=True, max_length=10)),
                ('charNullBlank', models.CharField(blank=True, max_length=10, null=True)),
                ('charBlankUnique', models.CharField(blank=True, max_length=10, unique=True)),
                ('charNullBlankUnique', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('intNull', models.IntegerField(null=True)),
                ('intBlank', models.IntegerField(blank=True)),
                ('intNullBlank', models.IntegerField(blank=True, null=True)),
                ('dateNull', models.DateTimeField(null=True)),
                ('dateBlank', models.DateTimeField(blank=True)),
                ('dateNullBlank', models.DateTimeField(blank=True, null=True)),
                ('boolBlank', models.BooleanField()),
                ('nullboolNull', models.NullBooleanField()),
                ('nullboolBlank', models.NullBooleanField()),
                ('nullboolNullBlank', models.NullBooleanField()),
            ],
        ),
    ]
