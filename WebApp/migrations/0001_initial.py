# Generated by Django 2.2.7 on 2019-11-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpID', models.IntegerField()),
                ('EmpName', models.CharField(max_length=40)),
                ('EmpSal', models.IntegerField()),
                ('EmpAdd', models.CharField(max_length=40)),
            ],
        ),
    ]