# Generated by Django 3.1.1 on 2020-10-10 19:50

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('stv', '0019_auto_20201010_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='date_persian',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ شمسی'),
        ),
    ]
