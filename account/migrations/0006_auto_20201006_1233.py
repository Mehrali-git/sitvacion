# Generated by Django 3.1.1 on 2020-10-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201006_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch_Id',
            field=models.CharField(max_length=20, null=True, verbose_name='کد شعبه'),
        ),
        migrations.AlterField(
            model_name='user',
            name='branch_name',
            field=models.CharField(max_length=100, null=True, verbose_name='نام شعبه'),
        ),
    ]
