# Generated by Django 3.1.1 on 2020-10-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stv', '0020_auto_20201010_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='branch',
            field=models.CharField(default='bmi', max_length=20, verbose_name='شعبه'),
        ),
    ]
