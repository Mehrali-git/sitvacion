# Generated by Django 3.1 on 2020-09-01 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200827_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='کاربر ویژه تازمان'),
        ),
    ]
