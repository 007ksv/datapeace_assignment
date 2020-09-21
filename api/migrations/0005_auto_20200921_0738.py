# Generated by Django 3.1.1 on 2020-09-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200920_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='company_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='web',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
    ]
