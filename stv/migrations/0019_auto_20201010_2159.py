# Generated by Django 3.1.1 on 2020-10-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stv', '0018_auto_20201010_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='total',
            field=models.CharField(default=0, max_length=100, verbose_name='مانده صندوق'),
        ),
    ]